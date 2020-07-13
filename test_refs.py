from pathlib import Path
import openpyxl

def test_refs_errors():
    sheets_with_refs = []
    for path in Path(__file__).parent.rglob('[!~]*.xls*'):
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for sheet in wb.worksheets:
            values = []
            for row in sheet.rows:
                values.append([cell.value for cell in row])
            if any('#REF!' in row for row in values):
                sheets_with_refs.append(f'{path.name}: {sheet.title}')
        wb.close()  # doesn't close automatically with read_only=True

    assert sheets_with_refs == []