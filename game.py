
import boardreader as br
import evaluation as ev

hextable = br.InitTable()
sc = ev.ScoreCalculator(hextable)
(blueScore, blueIslands, redScore, redIslands) = sc.CalculateScore()
print(sc.GetAverageSizeScore('b'))
# print(sc.GetDistances('b'))
sc.GetNeighborsScore('b')




