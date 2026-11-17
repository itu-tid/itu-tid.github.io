/** @OnlyCurrentDoc */ // the script may touch this one spreadsheet, nothing else in Drive
// Storage for the Extract Hunt: one row per answer in the sheet this script is bound to.
// Deploy: Extensions → Apps Script, paste this, Deploy → New deployment → Web app,
// execute as Me, access Anyone. Put the /exec URL in ENDPOINT in sheets.js.

const COLUMNS = ["time", "run", "code", "client", "seconds", "picks"];

function sheet_() {
  const s = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  if (s.getLastRow() === 0) {
    s.appendRow(COLUMNS);
    s.getRange("B:B").setNumberFormat("@"); // keep "2026-11-19" text, not a date
  }
  return s;
}

// the student page posts one answer; picks is a JSON list of {from, to, name}
function doPost(e) {
  const a = JSON.parse(e.postData.contents);
  sheet_().appendRow([new Date(), a.run, a.code, a.client, a.seconds, JSON.stringify(a.picks)]);
  return ContentService.createTextOutput("ok");
}

// the results page reads every answer of one run and one piece of code
function doGet(e) {
  const { run, code } = e.parameter;
  const rows = sheet_().getDataRange().getValues().slice(1)
    .filter((r) => String(r[1]) === run && r[2] === code)
    .map((r) => ({ client: r[3], seconds: r[4], picks: JSON.parse(r[5] || "[]") }));
  return ContentService.createTextOutput(JSON.stringify(rows))
    .setMimeType(ContentService.MimeType.JSON);
}
