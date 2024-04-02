#!/usr/bin/perl

use CGI qw(:standard);

print header();
print start_html("Current Date and Time");
print "<h1>Current Date and Time</h1>";

# Get current date and time
my ($sec, $min, $hour, $mday, $mon, $year) = localtime();
$year += 1900; # Adjust year to display correctly
$mon += 1;     # Adjust month to display correctly

# Format the date and time
my $current_datetime = sprintf("%04d-%02d-%02d %02d:%02d:%02d", $year, $mon, $mday, $hour, $min, $sec);

# Display the date and time in HTML
print "<p>The current date and time is: $current_datetime</p>";

print end_html();