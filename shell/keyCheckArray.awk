#!/usr/bin/awk

BEGIN{
}
{
    colors["red"]=1;
}
END{
    print colors;
}

