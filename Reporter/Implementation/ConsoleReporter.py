from Reporter.Reporter import Reporter
from Service.LoggerService.Implementation.DefaultPythonLoggingService import DefaultPythonLoggingService as Logger



class ConsoleReporter(Reporter):
    @staticmethod
    def report(data):
        print()
        Logger.info(__file__, 'Start reporting')

        print()
        print('========== REPORT ==========')

        for key in data:
            print(key, data[key])

        print('========== REPORT END ==========')
        print()
        Logger.info(__file__, 'Reporting finished')
        print()
