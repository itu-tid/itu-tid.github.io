// The two versions of todo-26's ToDoList.jsx, with the same bug planted in each:
// the Delete button is wired to toggle, so it checks the to-do off.
//   A: everything inline (loading and the three handlers)
//   B: loading and the handlers extracted into a useTodos(list) hook

// Set after deploying apps-script.gs as a web app.
const ENDPOINT = "https://script.google.com/macros/s/AKfycbx5Vrq3TH5NX16CVWBL_6YkYnrLy2JtjrQPFY52wZpfJsAy7z9TkoceS3PtdMPWIFCP0w/exec";

const SHEETS = {
  A: {
    bugText: "onDelete={handleToggle}",
    code: `import { useEffect, useState } from "react";
import AddForm from "../UI/AddForm.jsx";
import ToDoItem from "./ToDoItem.jsx";
import {
  loadTodos,
  addTodo,
  deleteTodo,
  setDone,
  canWrite,
} from "../../services/todoService.js";

// one list's to-dos: load them, add, delete, check off
export default function ToDoList({ list }) {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    loadTodos(list)
      .then(setTodos)
      .catch((error) => alert(error.message));
  }, [list]);

  async function handleAdd(text) {
    try {
      const todo = await addTodo(list, text);
      setTodos([...todos, todo]);
    } catch (error) {
      alert(error.message);
    }
  }

  async function handleDelete(id) {
    try {
      await deleteTodo(id);
      setTodos(todos.filter((each) => each.id !== id));
    } catch (error) {
      alert(error.message);
    }
  }

  async function handleToggle(id) {
    const todo = todos.find((each) => each.id === id);
    try {
      await setDone(id, !todo.done);
      setTodos(todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
    } catch (error) {
      alert(error.message);
    }
  }

  return (
    <>
      <h1>{list.get("name")}</h1>
      {todos.length === 0 ? (
        <p>Nothing to do</p>
      ) : (
        <ul>
          {todos.map((todo) => (
            <ToDoItem
              key={todo.id}
              todo={todo}
              onDelete={handleToggle}
              onChange={handleToggle}
            />
          ))}
        </ul>
      )}
      {canWrite(list) && <AddForm onAdd={handleAdd} buttonLabel="Add" />}
    </>
  );
}`,
  },
  B: {
    bugText: "onDelete={toggle}",
    code: `import AddForm from "../UI/AddForm.jsx";
import ToDoItem from "./ToDoItem.jsx";
import { useTodos } from "../../hooks/useTodos.js";
import { canWrite } from "../../services/todoService.js";

// one list's to-dos: load them, add, delete, check off
export default function ToDoList({ list }) {
  const { todos, add, remove, toggle } = useTodos(list);

  return (
    <>
      <h1>{list.get("name")}</h1>
      {todos.length === 0 ? (
        <p>Nothing to do</p>
      ) : (
        <ul>
          {todos.map((todo) => (
            <ToDoItem
              key={todo.id}
              todo={todo}
              onDelete={toggle}
              onChange={toggle}
            />
          ))}
        </ul>
      )}
      {canWrite(list) && <AddForm onAdd={add} buttonLabel="Add" />}
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
