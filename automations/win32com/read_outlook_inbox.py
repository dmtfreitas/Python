
# coding: UTF-8

# read_outlook_inbox.py

import win32com.client
import time

accounts = [
    'demetrio.oliveira@nunofracht.com.br',
    'Inovação',
    'Noreply'
]

INTERVAL = 10.5

def mark_email_as_read ():
    
    outlook = win32com.client.Dispatch ('Outlook.Application')
    namespace = outlook.GetNamespace ('MAPI')
    
    while True:

        for account in accounts:
            
            try:

                path_account = namespace.Folders.Item (account)

                inbox = path_account.Folders.Item ('Caixa de Entrada')

                emails = inbox.Items.Restrict ('[Unread] = True')

                quantity = emails.Count
                
                if quantity == 0:
                    
                    print (f'{account}: 0 unread emails! Waiting...')
                    continue

                for count in range (quantity, 0, -1):
                    
                    email = emails.Item (count)
                    email.UnRead = False

                print (f'{account}: {quantity} mark emails as read...')

            except Exception as error:
                
                print (f'Error in account - {account}: {error}')
                
        print('Checking accounts again...')
        time.sleep (INTERVAL)

if __name__ == '__main__':
    
    mark_email_as_read ()

