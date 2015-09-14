
$currentDirectory = Get-Location


$finalName = $currentDirectory.Path+"/script.downloadorganizer.zip"
$rootFolder = $currentDirectory.Path+"/script.downloadorganizer"
$topFolder = $currentDirectory.Path

cd $rootFolder
$result = python.exe -m unittest discover -s script.downloadorganizer test 2>&1 
$errorMsg =""+$result.Exception

cd $topFolder

If ($errorMsg.trim().endswith("OK")){
	
	function ZipFiles( $zipfilename, $sourcedir )
	{
	   Add-Type -Assembly System.IO.Compression.FileSystem
	   $compressionLevel = [System.IO.Compression.CompressionLevel]::Fastest
	   [System.IO.Compression.ZipFile]::CreateFromDirectory($sourcedir,
	        $zipfilename, $compressionLevel, $true)
	}
	
	If (Test-Path $finalName){
		Remove-Item $finalName
	}
	
	ZipFiles $finalName $rootFolder
}