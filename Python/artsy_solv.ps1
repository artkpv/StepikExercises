
$token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0Nzg2MDQ0MjIsImlhdCI6MTQ3Nzk5OTYyMiwiYXVkIjoiNTgxODdiMzAyNzViMjQxMjk3MDAwNDg5IiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjU4MTg3YzA2YjIwMmEzNjU4ODAwMDAxYyJ9.jL7UMr6vz89ZcOlKBle_PE5gHTIGMRFvEbXM33s20_0' 
chcp 65001; 
$arts = New-Object System.Collections.ArrayList; 
"
4d8b92b34eb68a1b2c0003f4
537def3c139b21353f0006a6
4e2ed576477cc70001006f99
" -split "`n" | ? {$_ -ne '' -and $_ -ne $null } | %{ 
  $url = "https://api.artsy.net/api/artists/$_"
  write-host $url
  $response = ""
  curl -s $url -H "X-Xapp-Token:$token" -k
  
  $null | %{ 
	  write_host $_
    
    $name = [regex]::Match($_, 'sortable_name":"([^"]+)"').Groups[1].Value

    $bd = [regex]::Match($_, 'birthday":"([^"]+)"').Groups[1].Value
    $arts.Add($bd + $name) > $null
   }
}; 
write-host $arts
$arts | ? { $_.length -gt 4 } | sort | %{ $_.substring(4) } 
