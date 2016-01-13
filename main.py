import urllib2
import json
import wx

y = 1

def currencyConverter(fran,till,valuta_mangd):
    #valuta_mangd = 1
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

fran='USD'
till = 'eur'
valuta_mangd = 1
#currencyConverter(fran,till,valuta_mangd)

rate = currencyConverter(fran,till,valuta_mangd)
#print rate



class WindowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WindowClass, self).__init__(*args, **kwargs)
        self.basicGUI()

    def basicGUI(self):
        menu_bar = wx.MenuBar()
        panel = wx.Panel(self)
        filebutton = wx.Menu()
        editButton = wx.Menu()
        exit_item = filebutton.Append(wx.ID_EXIT, 'Exit', 'Status msg')
        menu_bar.Append(filebutton, 'File')
        menu_bar.Append(editButton, 'Currencies')

        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.Quit, exit_item)
        x = wx.TextEntryDialog(None, 'From what currency', 'Currencies', 'EXAMPLE: USD,EUR')
        if x.ShowModal() == wx.ID_OK:
            currencies = x.GetValue()
            fran = currencies.lower().split(",")
        currencyConverter(fran[0],fran[1],1)
        wx.StaticText(None,-1,rate)
        self.SetTitle('Currency converter')
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    WindowClass(None)
    app.MainLoop()
main()
