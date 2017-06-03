Write-Host 'AAB -> ABA:'
"AAB" | py -3 get_palindrom.py

Write-Host 'QAZQAZ -> AQZZQA:'
"AQZZQA" | py -3 get_palindrom.py

Write-Host 'ABCDEFGHIJKLMNOPQRSTUVWXYZ -> M:'
"ABCDEFGHIJKLMNOPQRSTUVWXYZ" | py -3 get_palindrom.py

Write-Host 'QQQAZQAZ -> AQQZZQQA:'
"QQQAZQAZ" | py -3 get_palindrom.py

Write-Host 'QQQQAZQAZ -> AQQZZQQA:'
"QQQQAZQAZ" | py -3 get_palindrom.py

Write-Host 'AAABB -> ABABA:'
"AAABB" | py -3 get_palindrom.py
