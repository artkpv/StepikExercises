$tests = @(
"ababa
a
b",

"ababa
b
a",

"ababa
c
c",

"ababac
c
c",

"ababa
ab
ba",

"abbbb
a
ab"
)

$tests | %{ 
	Write-Host "Test: '$_':"
	$_ | py -3 stepik.py
}
