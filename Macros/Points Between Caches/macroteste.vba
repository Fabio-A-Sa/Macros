Function ArcCos(RadAngle)
    ArcCos = Atn(-RadAngle / Sqr(-RadAngle * RadAngle + 1)) + 2 * Atn(1)
End Function


Sub Caracol()

' Macro para GC92dgw

Dim i As Integer
Dim n As Integer
Dim w As Integer

Dim Lat1 As Integer
Dim Lat2 As Integer
Dim Long1 As Integer
Dim Long2 As Integer

Dim LatP As Double
Dim LongP As Double

Dim dblAcos As Double
i = 22

' "=ACOS(COS(RADIANS(90-R[-5]C[-2]))*COS(RADIANS(90-R[-4]C[12]))+SIN(RADIANS(90-R[-5]C[-2]))*SIN(RADIANS(90-R[-4]C[12]))*COS(RADIANS(R[-5]C[-1]-R[-4]C[13])))*6371"
    
For n = 580 To 620
        
        For w = 350 To 430
        Range("A" & i).Value = 41 + (4 + n / 1000) / 60
        Range("B" & i).Value = 8 + (35 + w / 1000) / 60
        ' Range("C" & i).Value = Acos(Cos(Pi * (90 - "A4") / 180) * Cos(Radians(90 - "O5")) + Sin(Radians(90 - "A4")) * Sin(Radians(90 - "O5")) * Cos(Radians("P4" - "P5"))) * 6371
        
        
        Range("H" & i).Value = "N 41° 04." & n & " W 008° 35." & w
        i = i + 1
        
        Next w
        


Next n



End Sub

