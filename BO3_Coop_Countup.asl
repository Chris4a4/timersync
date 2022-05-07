state("BlackOps3") 
{
	int round : 0x1140FC30;
	string13 currentMap : 0x180FFB20;
}

init
{
	refreshRate = 100;
}

start
{
	return true;
}

isLoading
{
	string[] arrayMaps = {"zm_zod", "zm_factory", "zm_castle", "zm_island", 
		"zm_stalingrad", "zm_genesis", "zm_prototype", "zm_asylum", "zm_sumpf", 
		"zm_theater", "zm_cosmodrome", "zm_temple", "zm_moon", "zm_tomb"};
		
	return Array.IndexOf(arrayMaps, current.currentMap) == -1 || current.round == 0;
}