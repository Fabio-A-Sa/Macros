Sub Normalization()

'
' Macro that deals with formatting the table and data imported from the
' Python script in order to be more easily viewed.
'

    Sheets(1).Select
    Folha1.Unprotect "password"
    Application.ScreenUpdating = False
    
    Columns("A:E").Select
    Selection.Columns.AutoFit

    ' Auto delimited size of columns
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

    ' Auto xlCenter
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

    ' Header Bold
    Rows("1:1").Select
    Selection.Font.Bold = True
    Columns("A:A").Select
    Selection.Font.Bold = False
    Selection.Font.Bold = True
    Range("A1:E1,A2:E21").Select
    Range("A2").Activate
    Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone

    ' Header gray
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .ColorIndex = xlAutomatic
        .TintAndShade = 0
        .Weight = xlThick
    End With

    ' First column gray
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .ColorIndex = xlAutomatic
        .TintAndShade = 0
        .Weight = xlThick
    End With


    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .ColorIndex = xlAutomatic
        .TintAndShade = 0
        .Weight = xlThick
    End With
    
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .ColorIndex = xlAutomatic
        .TintAndShade = 0
        .Weight = xlThick
    End With

    With Selection.Borders(xlInsideVertical)
        .LineStyle = xlContinuous
        .ColorIndex = xlAutomatic
        .TintAndShade = 0
        .Weight = xlThin
    End With

    With Selection.Borders(xlInsideHorizontal)
        .LineStyle = xlContinuous
        .ColorIndex = xlAutomatic
        .TintAndShade = 0
        .Weight = xlThin
    End With

    Range("B1:E1,A1:A21").Select
    Range("A1").Activate
    ActiveWindow.SmallScroll Down:=-30

    ' Center and Middle
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .ThemeColor = xlThemeColorDark1
        .TintAndShade = -0.349986266670736
        .PatternTintAndShade = 0
    End With

    Folha1.Protect "password"
    Application.ScreenUpdating = True
    ActiveWorkbook.Save
    
    MsgBox ("Macro successfully executed")

End Sub
