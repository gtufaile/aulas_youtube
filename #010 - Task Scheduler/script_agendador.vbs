Dim appExcel

Set appExcel = CreateObject("Excel.Application")
appExcel.Visible = False

Set arquivo = appExcel.Workbooks.Open("C:\Users\GUILHE~1\OneDrive\READET~1\Aulas\LI9AA2~1\Msg_Agendador.xlsm")
appExcel.Run "msg_agendador"
appExcel.Application.Quit



