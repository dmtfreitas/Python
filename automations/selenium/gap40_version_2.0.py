
# coding: UTF-8

# gap40_version_2.0.py

import re
import sys
from urllib.parse import urljoin
from curl_cffi import requests as creq

BASE = 'https://nunofracht.gap40.com.br'
LOGIN_URL = f'{BASE}/default.asp'

EXECUTAR_BATIDA = False

CPF = '12345678910'
SENHA = '12345678910'

PAYLOAD_FIXO = {
    'acao': '1',
    'cboCampo': '2',
    'chkAdicPer': '1',
    'chkAdicIns': '1',
    'chkAdicEmb': '1',
    'LOCALIZACAO': '',
}

def cookie (session, name):
    
    try:
        
        return session.cookies.get (name)
        
    except Exception:
        
        return None


def obter_captcha (session):

    raise_status = session.get (BASE + "/")
    
    raise_status.raise_for_status ()

    if cookie (session, 'ASPCAPTCHA'):
        
        return cookie (session, 'ASPCAPTCHA')

    html = raise_status.text

    refs = re.findall (r'(?:src|href)\s*=\s*["\']([^"\']+)["\']', html, re.I)
    
    candidates = []
    
    for ref in refs:
        
        if 'captcha' in ref.lower () and ref not in candidates:
            
            candidates.append (ref)

    for guess in ('captcha.asp', 'captcha.aspx', 'Captcha.asp', 'imgCaptcha.asp', 'captchaimage.asp'):
        
        if guess not in candidates:
            
            candidates.append (guess)

    print ('[*] ASPCAPTCHA did not appear GET | Testing candidates: ')
    
    for candidate in candidates:
        
        url = urljoin (BASE + '/', candidate)
        
        try:
            
            session.get (url)
            
        except Exception as error:
            
            print(f'{url} -> error: {error}')
            continue
        
        value = cookie (session, 'ASPCAPTCHA')
        mark = 'OK -> registered ASPCAPTCHA!' if value else 'not cookie'
        
        print (f'{url} -> {mark}')
        
        if value:
        
            return value

    print ('\n[!] Not candidate registered ASPCAPTCHA!')
    print ('Find the captcha image tag in the HTML below and let me know: ')
    print ('-' * 60)
    
    for linha in html.splitlines ():
        
        if 'captcha' in linha.lower () or '<img' in linha.lower ():
            
            print('   ', linha.strip ()[:200])
            
    print('-' * 60)
    
    return None

def clock_in (cpf, senha):
    
    session = creq.Session (impersonate='chrome')

    captcha = obter_captcha (session)
    
    if not captcha:
        
        sys.exit ('Aborted: CAPTCHA not solved!')

    print (f'\n[*] ASPCAPTCHA captured: {captcha}')

    if not EXECUTAR_BATIDA:
        
        print ('\n[*] EXECUTAR_BATIDA = False -> stoped before POST...')
        print ('ASPCAPCHA OK! Change to True to actually record...')
        
        return None

    payload = dict (PAYLOAD_FIXO)
    
    payload['txtValor'] = cpf
    payload['txtSenha'] = senha
    payload['captchacode'] = captcha

    raise_status = session.post (
        LOGIN_URL,
        data = payload,
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': BASE,
            'Referer': BASE + '/',
        },
    )
    raise_status.raise_for_status ()
    return raise_status


if __name__ == '__main__':
    
    response = clock_in (CPF, SENHA)
    
    if response is not None:
        
        print (f'\nStatus HTTP: {response.status_code}')
        print (f'response server: {response.text}')

