param($script =$(throw 'required'), $myargs = $null)
#$ErrorActionPreference = "Stop"

$global:counter = 0


function run-test {
	param([string]$inpt =$(throw 'required'), [string]$expected=$null, $name=$null,[switch] $toSkip = $false)
	$global:counter += 1
	$expected = $expected -join "`n"

	Write-Host "`n`n"
	Write-Host "--------- TEST $global:counter" ':' $name '-------------'
	Write-Host '        Input:'
	Write-Host $inpt
	#if($expected) {
	#	Write-Host '        Expected:'
	#	Write-Host $expected
	#}
	if($toSkip) {
		Write-Host 'SKIPPED'
		return
	}
	Write-Host '        Output:'
	$out = ""
	#$inpt | py $script $myargs | tee -Variable out 
	#$inpt | py $script $myargs #| tee -Variable out 
	$inpt | & $script $myargs #| tee -Variable out 
	if (-not $? ) { exit }

	$out = $out -join "`n"
	$out = $out -replace "`r",""
	$expected = $expected -replace "`r",""

	Write-Host '---------------------------'
	if (-not [string]::IsNullOrWhiteSpace($expected) ) {
		if(-not $out.trim().equals($expected.trim())){
			Write-Host '         FAILED'
			#Write-Host '     Input'
			#Write-Host $inpt
			Write-Host '         Expected:'
			Write-Host $expected
			#Write-Host '         Actual:'
			#Write-Host $out
			#exit
		} else {
			Write-Host '       SUCCESS'
		}
	} else {
	   Write-Host '     TEST FINISHED'
	   #Write-Host '     Input'
	   #Write-Host $inpt
	   #Write-Host '     Output'
	   #Write-Host $out
	}
}
