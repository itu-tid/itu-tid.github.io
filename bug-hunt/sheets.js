// The two versions of todo-26's Home.jsx, with the same bug planted in each:
// the Leave button calls onShare instead of onLeave.
//   A: week-08-service-layer (everything inline)
//   B: week-08-components (rows extracted into MyListRow and SharedListRow)

// Set after deploying apps-script.gs as a web app.
const ENDPOINT = "https://script.google.com/macros/s/AKfycbx5Vrq3TH5NX16CVWBL_6YkYnrLy2JtjrQPFY52wZpfJsAy7z9TkoceS3PtdMPWIFCP0w/exec";

const SHEETS = {
  A: {
    bugText: "onShare(membership)",
    code: `import { Link } from "react-router-dom";
import AddForm from "./AddForm.jsx";

// the home page: every list, by name, each one a link to its own page
export default function Home({
  lists,
  memberships,
  onAddList,
  onShare,
  onLeave,
  onLogout,
}) {
  return (
    <>
      <h2>My lists</h2>
      {lists.map((item) => (
        <div key={item.id}>
          <Link to={\`/lists/\${item.id}\`}>{item.get("name")}</Link>
          <AddForm
            onAdd={(username) => onShare(item, username)}
            buttonLabel="Share with (username)"
          />
        </div>
      ))}

      {memberships.length > 0 && <h2>Shared with me</h2>}
      {memberships.map((membership) => (
        <p key={membership.id}>
          <Link to={\`/lists/\${membership.get("list").id}\`}>
            {membership.get("list").get("name")}
          </Link>{" "}
          {/* include() leaves the owner out if I may not read that user's row */}
          shared by{" "}
          {membership.get("list").get("owner")?.get("username") ?? "someone"}{" "}
          <button onClick={() => onShare(membership)}>Leave</button>
        </p>
      ))}

      <br />
      <br />
      <h3>List Manager</h3>
      <AddForm onAdd={onAddList} buttonLabel="New list" />
      <h3>Account</h3>
      <button onClick={onLogout}>Logout</button>
    </>
  );
}`,
  },
  B: {
    bugText: "onLeave={onShare}",
    code: `import AddForm from "./AddForm.jsx";
import MyListRow from "./MyListRow.jsx";
import SharedListRow from "./SharedListRow.jsx";

// the home page: every list, by name, each one a link to its own page
export default function Home({
  lists,
  memberships,
  onAddList,
  onShare,
  onLeave,
  onLogout,
}) {
  return (
    <>
      <h2>My lists</h2>
      {lists.map((list) => (
        <MyListRow key={list.id} list={list} onShare={onShare} />
      ))}

      {memberships.length > 0 && <h2>Shared with me</h2>}
      {memberships.map((membership) => (
        <SharedListRow
          key={membership.id}
          membership={membership}
          onLeave={onShare}
        />
      ))}

      <br />
      <br />
      <h3>List Manager</h3>
      <AddForm onAdd={onAddList} buttonLabel="New list" />
      <h3>Account</h3>
      <button onClick={onLogout}>Logout</button>
    </>
  );
}`,
  },
};

// 1-based number of the line that holds the planted bug
function bugLine(sheet) {
  return linesOf(sheet).findIndex((l) => l.includes(SHEETS[sheet].bugText)) + 1;
}

function linesOf(sheet) {
  return SHEETS[sheet].code.split("\n");
}

function escapeHtml(text) {
  return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// Highlighted HTML, one string per line. The whole file is tokenized at once,
// because a JSX tag spans several lines, then the tokens are cut at each newline.
// Without Prism (the CDN did not load), the lines come back as plain text.
function highlightedLinesOf(sheet) {
  const code = SHEETS[sheet].code;
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
