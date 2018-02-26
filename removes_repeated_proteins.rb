# Line to execute
# "for x in `ls`; do ruby puniq.rb $x ; done"


sgname = ARGV[0]
sg = File.open(ARGV[0]).readlines
x = []

sg.each do |line|

	x << line
	x.sort!
    x.uniq!
end

puts x
puts sgname

File.open("PSG_#{sgname}", "w+") do |f|
	  			f.puts(x) 
end		
#Kernel.system("echo #{k}\t#{$sg.inspect} > SG_#{k}") if $sg.size > 1