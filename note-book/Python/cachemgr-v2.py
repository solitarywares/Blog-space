import os, logging, commands, time
import sys, traceback, random
import datetime, re, multiprocessing

#ASP source and own node IP list
servlist = {}
#servlist['guangzhou.asp.cntv.cn'] = [ '10.80.2.'+str(x) for x in range(127,142) ]
#servlist['jinan.asp.cntv.cn'] = [ '10.88.4.'+str(x) for x in range(126,141) ] + [ '10.88.2.'+str(x) for x in range(71,76) ]
servlist['beijing.asp.cntv.cn'] = [ '10.64.1.'+str(x) for x in range(35,45) ] + [ '10.64.2.'+str(x) for x in range(7,10) ] + ['10.64.2.5']
#servlist['beijing.backend.asp.cntv.cn'] = [ '10.64.0.127', '10.64.0.153', '10.64.0.17', '10.64.0.19', '10.64.0.20', '10.64.0.56', '10.64.1.51', '10.64.1.63', '10.64.1.65', '10.64.1.66', ]
#servlist['datong.backend.asp.cntv.cn'] = [ '10.78.48.' + str(x) for x in range(81,90) ]
#servlist['xuzhouzhou.backend.asp.cntv.cn'] =  [ '10.78.20.' +str(x) for x in range(15,23) ] + ['10.78.20.10', '10.78.20.5']
#servlist['jinan.backend.asp.cntv.cn'] = [ '10.70.83.' + str(x) for x in range(1,14) ]

#Defines the log module for log output
def get_logger(log_file, logger_name = None, level = logging.INFO):
    if not logger_name :
        import uuid
        logger_name = str(uuid.uuid1())

    log = logging.getLogger(logger_name)

    fmt = '%(asctime)s %(levelname)s => %(message)s'
    datefmt  = '%Y-%m-%d-%H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt)

    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    log.addHandler(fileHandler)

    log.setLevel(level)
    return log

#Parse the requested http format to generate the url of m3u8 and ts that needs to be cleared
def resolv_ts(urls) :
    clear_list = []
    for i in urls :
        ts_file = re.match('(.*)/(\d+)\.ts', i)
    	if ts_file :
            ts_list = [ ts_file.group(1)+'/'+str(m)+'.ts' for m in range(0,int(ts_file.group(2))+1) ]
            clear_list = clear_list + ts_list
        else:
            clear_list.append(i)
    return clear_list

#Generates a list of parameters that execute the clear cache command
#Example of a format that performs a clean command :curl -X PURGE -I -H Host:domain http://ip/url
def clear(url_list_clear) :
    for domain, servs in servlist.items() :
        args = []
    	for x in url_list_clear :
            for s in servs :
           	args.append((domain, s, x))
    	results = pool.map(clear_rmt_server, args)

#Call the function that clears the cache command
def clear_rmt_server(param) :
    domain, host, url = param
    try :
        outputport = commands.getstatusoutput('/usr/bin/nc -z -w 2 %s 80' % host)
        if list((outputport))[0] == 0:
            try :
                outputcache = commands.getstatusoutput('curl -X PURGE -I -H Host:%s http://%s%s' % (domain, host, url))
                outputcache_list = re.split('\n|\r\n', list((outputcache))[1])
                patten = ['HTTP/1.0 404 Not Found', 'HTTP/1.0 200 OK', 'HTTP/1.1 404 Not Found', 'HTTP/1.0 200 OK']
                result = '--'.join([host, url, outputcache_list[3]])
                if any(m in outputcache_list for m in patten):
                    logger.info(''' %s %s %s cache PURGE successful ! ''' % (domain, host, url))
                else:
                    logger.error(''' %s %s %s cache PURGE commands action exceptional ! ''' % (domain, host, url))
            except :
                logger.error(''' %s %s %s cache PURGE commands action fail ! ''' % (domain, host, url))
        else:
            logger.error(''' %s %s connect server port timeout ... ''' % (domain, host))
    except :
        logger.error(''' %s %s connect server port action fail ! ''' % (domain, host))
    return True

#Execute the main function
if __name__ == '__main__' :
    cachemgr_log = '/root/cachemgr.log'
    logger = get_logger(cachemgr_log)
    cacherequest = '/root/Url_clear'
    pool = multiprocessing.Pool(processes = 20)
    filename = "/root/cachemgr.postmak"
    while True :
        if os.path.isfile(filename):
            Jump_start = int(open(filename).read().strip())
            print Jump_start
        else:
            Jump_start = 0
            os.system(r'touch %s' % filename)
            os.system('echo "0" > %s' % filename)
        with open(cacherequest, 'r') as m :
            m.seek(Jump_start,0)
            clear_url = m.read()
            if clear_url:
                urls = clear_url.split('\r\n')
                url_list_clear = resolv_ts(urls)
                clear(url_list_clear)
                Jump_step = m.tell()
                os.system('echo "%s" > %s' % (Jump_step, filename))
            else :
                time.sleep(3)
