import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

print(time.ctime())



# 更改内置类
class cut(LoggingEventHandler):
    """Logs all the events captured."""
    def __init__(self, logger=None):
        super().__init__()

        self.logger = logger or logging.root

    def on_moved(self, event):
        super().on_moved(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Moved %s: from %s to %s", what, event.src_path,
                         event.dest_path)

    def on_created(self, event):
        super().on_created(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        super().on_deleted(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Deleted %s: %s", what, event.src_path)

    # log文件截取
    def on_modified(self, event):
        super(LoggingEventHandler, self).on_modified(event)
        what = 'directory' if event.is_directory else 'file'
        logging.info("Modified %s: %s", what, event.src_path)
        NameExt = event.src_path.split('.')
        if NameExt[-1] == 'log':
            os.system('powershell rm .\log\INFO.log.001')
            with open('./log/INFO.log', 'r') as fo:
                log = fo.read()
                shutdown = log.rfind('Shutting')
                if shutdown != -1:
                    with open('./README.md', 'r+') as fo:
                        fo.write(time.ctime() + ' ' + ' ' + '\n' +
                                 'Shutting down' + '\n')
                else:
                    tcp_position = log.rfind('server.natappfree.cc:')
                    print(tcp_position)
                    if tcp_position != -1:
                        tcp = log[tcp_position:tcp_position + 27]
                        print(tcp)
                        with open('./README.md', 'r+') as fo:
                            fo.write(time.ctime() + ' ' + ' ' + '\n' + tcp +
                                     '\n')
                        os.system(
                            'powershell git status ; powershell git commit -am "Updated" ; powershell git push origin master'
                        )
                    else:
                        pass
        print('(Ctrl+C to Quit)')
        


# watchdog运行
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    #生成事件处理器对象
    event_handler = cut()
    #生成监控器对象
    observer = Observer()
    #注册事件处理器，配置监控目录
    observer.schedule(event_handler, path, recursive=True)
    #监控器启动一创建线程
    observer.start()
    #以下代码是为了保持主线程运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    #等待其他的子线程执行结束之后，主线程再终止
    observer.join()