# Python 2.7 OAuth Connection to Outlook
Follow [Microsoft's documentation](https://docs.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth) to get the necessary parameters.

**Disclaimer: Python 2.7 is no longer supported. Only use this library if you have no way of updating to Python 3.**

[O365](https://o365.github.io/python-o365/latest/) is a free python package for Python 3.4 and later that simplifies connecting to Outlook via the MSGraph Protocol.


## Example usage

> from O365EasyEmail import O365Easy
> 
> starter = O365Easy()
> starter.Get_Token_Data('client/app_id', 'client_secret', 
> 'tenant_id', 'email@example.com', 'password')
> 
> values = starter.getMessages()
> print(values)
> 
### The below code will beautify the output of the dictionary to resemble JSON. Easier for human parsing
> import json
> print(json.dumps(values, indent = 4))

### The below will get ID to add to the list. If you want to make a custom dictionary you can do so in a loop like this
> idList = []
> for item in values:
>    print(item["from"]["emailAddress"]["address"])
>    idList.append(item['id'])

### This will delete given an id. You can loop through all messages/IDs
 > starter.deleteMessage(idList[-1])
