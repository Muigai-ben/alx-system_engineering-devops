# kill process killmenow

exec { 'pkill':
	command =>	'pkill killmenow' ,
	provide =>	'shell' ,
}
