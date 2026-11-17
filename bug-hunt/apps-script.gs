/** @OnlyCurrentDoc */ // the script may touch this one spreadsheet, nothing else in Drive
// Storage for the Bug Hunt: one row per answer in the sheet this script is bound to.
// Deploy: Extensions → Apps Script, paste this, Deploy → New deployment → Web app,
// execute as Me, access Anyone. Put the /exec URL in ENDPOINT in sheets.js.

const COLUMNS = ["time", "run", "sheet", "client", "seconds", "line", "found"];

function sheet_() {
  const s = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  if (s.getLastRow() === 0) {
    s.appendRow(COLUMNS);
    s.getRange("B:B").setNumberFormat("@"); // keep "2026-11-19" text, not a date
  }
  return s;
}

// the student page posts one answer
function doPost(e) {
  const a = JSON.parse(e.postData.contents);
  sheet_().appendRow([new Date(), a.run, a.sheet, a.client, a.seconds, a.line, a.found]);
  return ContentService.createTextOutput("ok");
}

// the results page reads every answer of one run
function doGet(e) {
  const run = e.parameter.run;
  const rows = sheet_().getDataRange().getValues().slice(1)
    .filter((r) => String(r[1]) === run)
    .map((r) => ({ sheet: r[2], client: r[3], seconds: r[4], line: r[5], found: r[6] === true }));
  return ContentService.createTextOutput(JSON.stringify(rows))
    .setMimeType(ContentService.MimeType.JSON);
}
