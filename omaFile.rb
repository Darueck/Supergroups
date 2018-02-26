class OmaFile

    attr_accessor :oma

    def initialize(file)
        oma = File.open(file).readlines

        # Creates a HASH for the result
        omaH = {}

        # reads the file, line by line
        oma.each do |line|
            # Ignore lines that begin with the #
            unless line =~ /^#/
                x = line.split("\t")
                id = x[0]
                tmp = []
                i = 1
                x.each do |p|
                    unless i == 1
                        tmp << p.gsub("\n",'')
                    end
                    i+=1
                end
                omaH[id] = tmp
            end
        end
        @oma = omaH
    end

    def inspect
        puts @oma.inspect
    end

    # Get Proteins By Group Id
    def getProteinsByGroupId(id)
       return @oma[id] 
    end

end