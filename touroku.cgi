if ($ENV{'REQUEST_METHOD'} eq 'POST') {
  read(STDIN, $alldata, $ENV{'CONTENT_LENGTH'});
} else {
  $alldata = $ENV{'QUERY_STRING'};
}
foreach $data (split(/&/, $alldata)) {
  ($key, $value) = split(/=/, $data);

  $value =~ s/\+/ /g;
  $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack('C', hex($1))/eg;
  $value =~ s/\t//g;

  $in{"$key"} = $value;
}

print "Content-Type: text/html; charset=Shift_JIS\n\n";
print "<html>\n";
print "<head><title>���͓��e</title></head>\n";
print "<body>\n";

#�󂯎�����f�[�^��\������
print "<p>���O: $in{'name'}</p>\n";
print "<p>URL: $in{'url'}</p>\n";

print "</body>\n";
print "</html>\n";

exit;