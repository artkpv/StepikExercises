$cmd = 'ex2.3.3maxtable.py'

$tests = @(
@(
'2
2
3
5
5
'
,
"5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3"
)
)

$tests | %{ 
	$_
	return
	$out = ( $_[0] | & python $cmd | out-string)
	if($out -ne $_[1])
	{ "FAILED:`n$($_[0])`n$($_[1])" }
	else { "SUCCESS" }
}
