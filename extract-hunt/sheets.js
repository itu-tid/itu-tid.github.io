// The code of the Extract Hunt: real components from this year's group projects,
// shown as they were in the repo (the Tasks page is cut to its first 130 lines of JSX),
// under a comment of ours that says what the code is and what is in scope.
// Students mark the lines they would extract into a component and name it.
// "ours" is the extraction we discuss afterwards, revealed on the results page.

// Set after deploying apps-script.gs as a web app.
const ENDPOINT = "https://script.google.com/macros/s/AKfycbwEvCRHOBFM1uPiVI2hw4gox8-RzrOo5KpuDeAf-Npv_7smpTneaswX8r192E7v_e9GnQ/exec";

const SNIPPETS = {
  meal: {
    file: "MealPlanDay.jsx",
    ours: [
      { from: 39, to: 44, name: "PlannedDish" },
      { from: 53, to: 65, name: "SuggestedDish" },
    ],
    code: `// One day of a family's weekly meal plan.
// Parents add dishes to the plan; children can only suggest them.
//   entries      the dishes planned for this day
//   suggestions  the dishes the children suggested for this day
//   dishes       every dish the family knows, for the dropdown
//   isParent     true when the logged-in user is a parent

import ChooseDishForm from "./ChooseDishForm.jsx";
import DishCard from "./DishCard.jsx";

export default function MealPlanDay({
  day,
  entries,
  dishes,
  onAdd,
  onRemove,
  suggestions,
  onDismiss,
  onAcceptSuggestion,
  onSuggest,
  isParent,
}) {
  return (
    <section>
      <h2>{day.toLocaleDateString("en-GB", { weekday: "long" })}</h2>
      {/* Parents add straight to the plan; children can only suggest */}
      <ChooseDishForm
        dishes={dishes}
        onChoose={(dishId) =>
          isParent ? onAdd(dishId, day) : onSuggest(dishId, day)
        }
        buttonLabel={isParent ? "Add" : "Suggest"}
      />
      {entries.length === 0 ? (
        <p>Nothing planned</p>
      ) : (
        <ul>
          {entries.map((entry) => (
            <li key={entry.id}>
              <DishCard dish={entry.dish} />
              {isParent && (
                <button onClick={() => onRemove(entry.id)}>Remove</button>
              )}
            </li>
          ))}
        </ul>
      )}
      {suggestions.length > 0 && (
        <>
          <h3>Suggested</h3>
          <ul>
            {suggestions.map((suggestion) => (
              <li key={suggestion.id}>
                <DishCard dish={suggestion.dish} />
                {isParent && (
                  <>
                    <button onClick={() => onAcceptSuggestion(suggestion)}>
                      Add to plan
                    </button>
                    <button onClick={() => onDismiss(suggestion.id)}>
                      Dismiss
                    </button>
                  </>
                )}
              </li>
            ))}
          </ul>
        </>
      )}
    </section>
  );
}`,
  },
  tasks: {
    file: "TasksPage.jsx",
    ours: [
      { from: 18, to: 37, name: "ChoiceGroup" },
      { from: 51, to: 73, name: "DayButton" },
      { from: 63, to: 72, name: "TaskDots" },
      { from: 95, to: 100, name: "TimeSlot" },
      { from: 111, to: 140, name: "ChoiceGroup" },
    ],
    code: `// The Tasks page of a chores app for a household of two.
// The page is 691 lines long; this is the first part of what it returns.
// Defined earlier in the page:
//   view, showList, showWeek          List or Week view, and how to switch
//   weekDays, shownDay, setPickedDay  the 7 days, the one picked, how to pick
//   tasksOn(date), dayTasks           the tasks of a date; of the picked day
//   household                         the two people: .owner and .partner
//   other                             the other person in the household
//   filter, showEveryone, showMine,   whose tasks the List shows,
//     showPartner                     and how to switch
//   slotTimeOf(task), renderTask(task)  helpers

  return (
    <>
      <h1 className="t-screen-title">Tasks</h1>

      {/* List | Week, as in Figma: List first */}
      <div className="tasks-page__views" role="group" aria-label="View">
        <button
          type="button"
          className="tasks-page__view t-body-strong"
          aria-pressed={view === "list"}
          onClick={showList}
        >
          <ListChecks size={18} aria-hidden="true" />
          List
        </button>
        <button
          type="button"
          className="tasks-page__view t-body-strong"
          aria-pressed={view === "week"}
          onClick={showWeek}
        >
          <CalendarDays size={18} aria-hidden="true" />
          Week
        </button>
      </div>

      {saveError && <p className="tasks-page__error t-meta">{saveError}</p>}

      {view === "week" && (
        <>
          <div className="tasks-page__week" role="group" aria-label="Day">
            {weekDays.map(function renderWeekDay(date) {
              // the same closure as chooseDay in TaskForm: each button knows its date
              function pickDay() {
                setPickedDay(date);
              }

              return (
                <button
                  key={date.getTime()}
                  type="button"
                  className="tasks-page__week-day"
                  aria-pressed={date.getTime() === shownDay.getTime()}
                  onClick={pickDay}
                >
                  <span className="t-chip">
                    {date.toLocaleDateString("en-GB", { weekday: "short" })}
                  </span>
                  <span className="t-body-strong">{date.getDate()}</span>
                  {/* one dot per task, in the colour of whoever does it */}
                  <span className="tasks-page__dots" aria-hidden="true">
                    {tasksOn(date).map((task) => (
                      <span
                        key={task.id}
                        className={\`tasks-page__dot tasks-page__dot--\${
                          task.assignedTo === household.owner.id ? "a" : "b"
                        }\`}
                      />
                    ))}
                  </span>
                </button>
              );
            })}
          </div>

          <SectionHeader
            title={shownDay.toLocaleDateString("en-GB", {
              weekday: "long",
              day: "numeric",
            })}
            count={dayTasks.length}
          />

          {dayTasks.length === 0 && (
            <p className="tasks-page__status t-body">
              Nothing planned this day.
            </p>
          )}

          {/* each row: the time on the left, the same card as in the List */}
          <div className="tasks-page__list">
            {dayTasks.map((task) => (
              <div key={task.id} className="tasks-page__slot">
                <span className="tasks-page__slot-time t-meta">
                  {slotTimeOf(task) || "Any time"}
                </span>
                {renderTask(task)}
              </div>
            ))}
          </div>
        </>
      )}

      {/* everything from here to "Done this week" is the List view */}
      {view === "list" && (
        <>
          {/* without a partner there is nobody to filter by */}
          {other && (
            <div
              className="tasks-page__filters"
              role="group"
              aria-label="Whose tasks"
            >
              <button
                type="button"
                className="tasks-page__filter t-body-strong"
                aria-pressed={filter === "everyone"}
                onClick={showEveryone}
              >
                Everyone
              </button>
              <button
                type="button"
                className="tasks-page__filter t-body-strong"
                aria-pressed={filter === "mine"}
                onClick={showMine}
              >
                Mine
              </button>
              <button
                type="button"
                className="tasks-page__filter t-body-strong"
                aria-pressed={filter === "partner"}
                onClick={showPartner}
              >
                {other.username}'s
              </button>
            </div>
          )}

          {/* ... the rest of the List view ... */}
        </>
      )}
    </>
  );`,
  },
};

function escapeHtml(text) {
  return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// Highlighted HTML, one string per line. The whole file is tokenized at once,
// because a JSX tag spans several lines, then the tokens are cut at each newline.
// Without Prism (the CDN did not load), the lines come back as plain text.
function highlightedLinesOf(key) {
  const code = SNIPPETS[key].code;
  if (!window.Prism || !Prism.languages.jsx) return code.split("\n").map(escapeHtml);

  const lines = [[]];
  function walk(token, classes) {
    if (typeof token === "string") {
      token.split("\n").forEach((part, i) => {
        if (i > 0) lines.push([]);
        if (!part) return;
        const html = escapeHtml(part);
        lines[lines.length - 1].push(
          classes.length ? `<span class="${classes.join(" ")}">${html}</span>` : html);
      });
      return;
    }
    // Prism reads JSX text as JavaScript, so "with" in "Shared with me" would
    // come out as a red keyword and draw the eye to the wrong line
    if (token.type === "keyword" && token.content === "with") return walk("with", classes);
    // the innermost token decides the color, as it would in nested spans
    const cls = ["token", token.type, ...[].concat(token.alias || [])];
    [].concat(token.content).forEach((child) => walk(child, cls));
  }
  Prism.tokenize(code, Prism.languages.jsx).forEach((t) => walk(t, []));
  return lines.map((parts) => parts.join(""));
}

// one round of the exercise: ?run=<label>, or today's date
function currentRun() {
  const fromUrl = new URLSearchParams(location.search).get("run");
  return fromUrl || new Date().toISOString().slice(0, 10);
}

// which code: ?code=meal or ?code=tasks
function currentSnippet() {
  const key = new URLSearchParams(location.search).get("code");
  return SNIPPETS[key] ? key : "meal";
}

function linesOf(key) {
  return SNIPPETS[key].code.split("\n");
}

// "Planned dish", "plannedDish" and "<PlannedDish />" are one name
function normalize(name) {
  return name.toLowerCase().replace(/[^a-z0-9]/g, "");
}
