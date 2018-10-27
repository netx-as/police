#!/usr/bin/perl -w 
# 
#
use strict;
use Data::Dumper;

my $POLICE_HELPER	= "/usr/bin/police-server-helper";
my $RESULT_DIR		= "/var/police/_postdata";

my ($ret, $fh, $ofh, $system);

print "Content-Type: text/html\n\n";

# get hostname 
if (!defined($ENV{'PATH_INFO'})) {
	printf "Mussing system name.\n";
	exit 0;
}

$system = $ENV{'PATH_INFO'};
$system =~ s/\///g;

if ($system =~ /^([\-\w\d\.]+)$/) {
	$system = $1;           # $data now untainted
} else {
	printf "Invalid characters in system name %s.", $system;
	exit 0;
}



my $cmd = sprintf("%s request %s", $POLICE_HELPER, $system);
$ret = open($fh, "$cmd|");
if (!$ret) {
	printf "%s\n", $!;
}

while (<$fh>) {
	print $_;
}
close $fh;	

# end script if there are no additional post data
if (!defined($ENV{'REQUEST_METHOD'}) || $ENV{'REQUEST_METHOD'} ne 'POST') {
	exit 0;
}

# process post data
my $resfile = sprintf("%s/%s", $RESULT_DIR, $system);

while (<>) {
	# open output file when first line arrives 
	if (!defined($ofh)) {
		$ret = open($ofh, "> $resfile");
		if (!$ret) {
			printf "Server Error: %s %s\n", $!, $resfile;
			exit 1;
		}
	}
	print $ofh $_;
}

close $ofh;
#printf Dumper(\%ENV);;


