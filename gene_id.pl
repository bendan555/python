open (FILE, "gene2accession");
open (OUT, ">id.txt");
print OUT ("gi\tgene_id\n");
$line=<FILE>;
while($line ne "")  
{
$line=<FILE>;
chomp($line);
@array=split(/\t/,$line);
if($array[0]==10090)
{
print OUT ("$array[6]\t$array[1]\n");
}
}
