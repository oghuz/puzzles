#!/usr/bin/perl -w

$name = $ARGV[0]; #it willl take test.txt file as input file 
open FILE , "<$name" or die $! ;
foreach $line(<FILE>) {
if($line =~ /([a-z]+[0-9]+.rec)/) {
print "the match $&\n" ;
print " after match $' \n" ;
print " before match $`\n" ;
}
}
close FILE ;

