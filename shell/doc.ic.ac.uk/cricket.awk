BEGIN{players=0;runs=0}
{if($4 != "not-out"){ players++;runs+=$3}}
END{print "avg run " runs/players }
