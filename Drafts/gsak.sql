# FAS GSAK

// Filter by status

$status = sqlite("sql",$_SqlGrid, "sqlget=yes")
$data = ""
while not($_sqleol)
  $data = $data + sqlget("code") + sqlget("name") + sqlget("userdata") + $_Crlf
  sqlnext
Endwhile

// Filter by dificulty

$test = "$d_Difficulty"

// Another filter

$data = sqlite("sql","Select * from caches where difficulty = $d_difficulty","")

// Order and sorted

$CurrentSort = $_OrderBy
#Change our sort sequence to do some work in our desired sequence
SQLSort OrderBy=Terrain Asc, Difficulty desc
# do some work here
#....
# Now finally restore our current sort sequence
SQLSort OrderBy=$CurrentSort

// _SqlGrid

$status = sqlite("sql",$_SqlGrid, "sqlget=yes")
$data = ""
while not($_sqleol)
  $data = $data + sqlget("code") + sqlget("name") + sqlget("userdata") + $_Crlf
  sqlnext
Endwhile

// today message

$sqlToday = DateToSql($_Today)
msgok msg=$SqlToday