"-----TEST ----"
"helloworld"

"hlelowrold
2
1 1 2
6 6 7" | % {
	write-host "           INPUT:"
	write-host $_;
	write-host "           OUTPUT:";
	$_ | py ex4.4.5rope.py $myargs 
	} 
