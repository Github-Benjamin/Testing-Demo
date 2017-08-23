import optparse

paser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
paser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
paser.add_option('-p', dest='tgtPort', type='int', help='specify target port')
(options, args) = paser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort
args.append(tgtPort)

print tgtHost
print tgtPort
print args

for i in range(len(args)):
    print tgtHost,args[i]
