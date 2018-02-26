class OrthoMCLType

    attr_accessor :type, :genes, :proteins, :taxa, :organisms

    def initialize(type)
        if type.class == Array
            @type = type
        else
            raise 'Type wrong!'
        end
    end

    # Number of proteins in group
    def genes
        return @type.size
    end

    # Number of Taxas
    def taxa
        tmp = []
        @type.each do |p|
            tmp << p.split('(')[1].split(')')[0]
        end
        tmp.sort!
        tmp.uniq!
        return tmp.size
    end

    # Array of Organisms
    def organisms
        tmp = []
        @type.each do |p|
            tmp << p.split('(')[1].split(')')[0]
        end
        return tmp
    end

    # Array of Proteins ID
    def proteins
        tmp = []
        @type.each do |p|
            tmp << p.split('(')[0]
        end
        return tmp
    end

    

end