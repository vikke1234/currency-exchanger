import wx

from yahoo_finance import Currency

'''
def currencyConverter(fran,till,valuta_mangd):
    #valuta_mangd =
    #fran = raw_input("Which currencies would you like to get the exchange rate from? Examples; EUR, USD\n")
    #till = raw_input("the second one\n")
    yql_base_url = "https://query.yahooapis.com/v1/public/yql"
    yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+fran+till+'")'
    yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    try:
        yql_response = urllib2.urlopen(yql_query_url)
        try:
            yql_json = json.loads(yql_response.read())
            currency_output = valuta_mangd * float(yql_json['query']['results']['rate']['Rate'])
            return currency_output
        except (ValueError, KeyError, TypeError):
            return "json format error"
    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason
#    rate = currencyConverter(fran,till,valuta_mangd)
fran='USD'
till = 'eur'
valuta_mangd = 1
#currencyConverter(fran,till,valuta_mangd)
#print rate
'''
crreny = Currency('usdeur')

class WindowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WindowClass, self).__init__(*args, **kwargs)
        self.basicGUI()

    def basicGUI(self):
        #items
        menu_bar = wx.MenuBar()
        filebutton = wx.Menu()
        editButton = wx.Menu()
        currencyButton = wx.Menu()

        #under construction below

        #currencyItem = currencyButton.Append()
        exitItem = filebutton.Append(wx.ID_EXIT, 'Exit', 'Exit application')
        menu_bar.Append(filebutton, '&File')
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        self.Show(True)
        self.CreateStatusBar()
        panel = wx.Panel(self)
        #panels and stuff



        self.quote = wx.StaticText(panel, label=crreny.get_rate(), pos=(20, 30))


        self.SetTitle('Currency converter')
        #self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    WindowClass(None)
    app.MainLoop()
main()