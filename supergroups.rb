#!/usr/bin/env ruby

# Line to execute
#
# To show only the totals:
#    ruby supergroups.rb all_orthomcl_3_taxa.out OrthologousGroups.txt
#
#
#

require './orthomclFile.rb'
require './orthomclType.rb'
require './omaFile.rb'
require './omaType.rb'

$parserMcl = OrthoMCLFile.new(ARGV[0])
$parserOma = OmaFile.new(ARGV[1])
file = ARGV[2] unless ARGV[2].nil?

$mcl = $parserMcl.mcl
$oma = $parserOma.oma

puts "Preparando ."
# Groups of MCL with 2 and 3 genes equal to those of OMA
iguais = []
print '..'
$mcl.each do |k, v|
	regMcl = OrthoMCLType.new(v)
	pMCL = regMcl.proteins
	if regMcl.genes == 3
		print "."
		$oma.each do |k1, v1|
			regOma = OmaType.new(v1)
			pOMA = regOma.proteins
			iguais << k if pMCL == pOMA
		end
	end
end

iguais2 = []
print '..'
$mcl.each do |k, v|
	regMcl = OrthoMCLType.new(v)
	pMCL = regMcl.proteins
	if regMcl.genes == 2
		print "."
		$oma.each do |k1, v1|
			regOma = OmaType.new(v1)
			pOMA = regOma.proteins
			if regOma.genes == 2
				iguais2 << k if pMCL == pOMA
			end
		end
	end
end


def find(type, id)
	puts "Find id: #{id} and Type #{type}"
	if id.nil?
		puts "Terminou recursividade"
		return id
	else
		if type == 1 # Search in OMA
			puts "Buscando no OMA"
			# Grab MCL Proteins
			regMCL = OrthoMCLType.new($parserMcl.getProteinsByGroupId(id))
			pMCL = regMCL.proteins
			$oma.each do |k1, v1|
				regOma = OmaType.new(v1)
				pOMA = regOma.proteins
				if (pMCL & pOMA) != []
					puts "Encontrou no OMA, indo para o find MCL"
					unless $sg.include?(k1)
						$sg << k1 
						find(2, k1) 
					end
				end
			end
			puts "Nao encontrou no OMA"
			return nil
		elsif type == 2   # BSearch in MCL
			puts "Buscando no MCL"
			# Grab OMA Proteins
			regOMA = OmaType.new($parserOma.getProteinsByGroupId(id))
			pOMA = regOMA.proteins
			$mcl.each do |k1, v1|
				regMcl = OrthoMCLType.new(v1)
				pMCL = regMcl.proteins
				if (pOMA & pMCL) != []
					puts "Encontrou no MCL, indo para o find OMA"
					unless $sg.include?(k1)
						$sg << k1 
						find(1, k1)
					end
				end
			end
			puts "Nao encontrou no MCL"
			return nil
		end
	end
end


# Groups with some intersection without equals (2 and 3 genes)
puts "Criando Super-Grupos MCL x OMA ."
print '..'
usados = iguais + iguais2
Kernel.system("echo #{usados} > iguais.txt")
$mcl.each do |k, v|
	regMcl = OrthoMCLType.new(v)
	pMCL = regMcl.proteins
	print "."
	if not usados.include?(k)
		$sg = []
		$sg << k
		achou = find(1, k)
		puts "#{k}: #{$sg.inspect}" if $sg.size > 1
		#Kernel.system("echo #{k}\t#{$sg.inspect} > SG_#{k}") if $sg.size > 1

	end
	
end
