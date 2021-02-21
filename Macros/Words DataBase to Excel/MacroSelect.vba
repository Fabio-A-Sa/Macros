Sub TitleMacro()

'
' Macro (...)
'

    Sheets(1).Select
    Folha1.Unprotect "password"
    Application.ScreenUpdating = False

    ' Some code

    Folha1.Protect "password"
    Application.ScreenUpdating = True
    ActiveWorkbook.Save
    
    MsgBox ("Macro successfully executed")

End Sub