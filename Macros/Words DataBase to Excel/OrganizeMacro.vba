Sub Organize()

'
' Macro that organizes cells for better data reading
'

    Sheets(1).Select
    Folha1.Unprotect "password"
    Application.ScreenUpdating = False

    Columns("A:J").Select
    Selection.Columns.AutoFit

    With Selection
        .HorizontalAlignment = xlGeneral
        .VerticalAlignment = xlCenter
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With

    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlCenter
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With

    Rows("1:2").Select
    Selection.Font.Bold = True

    Folha1.Protect "password"
    Application.ScreenUpdating = True
    ActiveWorkbook.Save
    
    MsgBox ("Macro successfully executed")

End Sub

