Sub stockVolume()
Dim ws As Worksheet
Set ws = Sheets(1)
For Each ws In Worksheets
Dim ticker As String
Dim totalVolume As Double
Dim Sumrow As Double
Dim lastRow As Double
Sumrow = 2
totalVolume = 0
lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

ticker = ws.Cells(2, 1).Value
For i = 2 To lastRow
   If ticker = ws.Cells(i + 1, 1).Value Then
       totalVolume = totalVolume + ws.Cells(i, 7).Value
   Else
       totalVolume = totalVolume + ws.Cells(i, 7).Value
   ws.Range("I1").Cells(1, 1).Value = "ticker"
   ws.Range("I1").Cells(1, 2).Value = "totalVolume"
   ws.Range("I1").Cells(Sumrow, 1).Value = ticker
   ws.Range("I1").Cells(Sumrow, 2).Value = totalVolume
   Sumrow = Sumrow + 1
   totalVolume = 0
   ticker = ws.Cells(i + 1, 1).Value
   End If
 Next i
Next ws
End Sub
