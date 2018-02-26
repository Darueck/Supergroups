class OrthoMCLFile

    attr_accessor :mcl

    def initialize(file)
        mcl = File.open(file).readlines

        # Creates a HASH for the result
        mclH = {}

        # reads the file, line by line
        mcl.each do |line|

            # Get the ID of the orthographic group
            id = line.split(':')[0].split('(')[0]
        
            # Creates an array for the group's proteins
            mclH[id] = line.split(':')[1].split(" ")
        end
        @mcl = mclH
    end

    def inspect
        puts @mcl.inspect
    end

    # Get Proteins By Group Id
    def getProteinsByGroupId(id)
        return @mcl[id] 
    end

end