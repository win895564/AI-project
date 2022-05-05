# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:27:15 2022

@author: user
"""

from selenium import webdriver
from openpyxl import Workbook 
import re
import requests
from requests_html import HTMLSession
import time
dict01={'台中市大甲區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/3260d10ef929853e1074f955e7aeb3fc?q=VTJGc2RHVmtYMTlZUEI0ajRsRFo4NEczMzU3aUJFMUFnZlpHdmtrbzFiN25XOGZIalgwRlQ5MGJzSEZuOUZvTEs0Q2x4RFcyb3JFWG9uVmRyMlUxS0tMZmtCcFdLTGFPWWd1aHRNSmxKNzJRL3FNMjZVTWFQNVVTSjFWc2JhWnloazB6Mzh3OFI0eXNBVDVVUGpKZDhSVnRYejV5ZHRnWXEvSFFqc21CZGNYYlNGWjJNZFB6V09zRUhpU1pQTFhhSXpyYWlRcEF0UXAxV3NkZUJHRFhHWnhFMkoxTDNoWTlNd0VRYzkxd1pHRlFzVXRzUFpON3lhNkVOZWtlWTMxaW8yZ3BXcUFCQkIxR3FPYjVvek5oRWh2RUZBb2c5anZKdnk0MlE5OXNSamorUm4xcUIrVjJnMUUxTU5EMkFDZFNISk1GM29BUFhJZEhHM09BUE1mNDM0d3lNTkhKSllkUS9WYUxnMXQ1UXBCRlpEZnZSWDVidTllMm5jZzhzRU9SdmdNR3R0RFYrTmFTMFEwc3NpNGVPU20vN0ZNbXQ3QVZJN01yTWxGK3U0dC96ZXB0RnpXOU9ES3BaRlQrbUFKeFMydXhQT1ExTFBVeVhOQjZLN2g3ZlRZRHMxWlBsczVod3V1dEdmN3ArYjNBQ09BQ3BZWlpPc1pqQS9uekNhdTJ1YVJLNG9qVkVkSUl4UC9HL1NWWlFoMis0ckhvdFpjZGNYUExIL0hGT0Q0PQ=="\
           ,'台中市大安區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/53c8feb86fb3141ba10a1b04392858b1?q=VTJGc2RHVmtYMSsvOEkxKzVnQW04TTA3MWh5cnNuNlYyd1lISVl2QjBvZXF2enV6RUNnZlUxcCtJZ2dTdHhROTdNY3JMaklGVURvNFpDTlcwczhrSWVmUHFCanVSYklIRG5RM0NhcGNmZFJhQ2ZKRDAwdnVhR3hmNXRxcTFJMVpwamRYRzVWdGdESkVJVnBLRGVQYkVkeUVnK0ZROFJwalJyZ2JEVE9lYzNrNGQ5eURJTE5IaXRFUmYvSmZneEh5dEZkM0Y3dTJ5Tk9LR0lNNVBnem1OVTM2emtwVFQ2UTFEanNmSm1hNzluQTdxMG5lTkdEOW5EQnNlb0g2WEFXS0s5YnlRUGEycWpNUEc0Z05xbzcrY2ZlK0p1a2FaYXdqMUgrS1BSM3JpN3J1L2hIQ256eWN1dHV4QmNxUEppY201eVFEdHN2dndEQUNTR0FELzBhTUl4bzNJa2VseW1xTHlMR1EzS3BVdnB2ZUJ0eFRHblFyT1Nndlo1bk5uRFpUKzhSQUlHRjU1UnE1R254c05mNUJXRUl3SjNKcWQ4M3BFbjdQZS9pejMyUzFPcTNqVG1xMjBGRDFaQ3NjU3hjQXE5UUp3R1kvYlVFaDh1bXpnR05nTUFta0pCZC9xK1NHbnd2SXJtN3pBKzZ2UUs3OXh5YTFQSEwyWG1idmpvcjlwTGRpOU1hUzJyVkQ4OFNoM0JtMmJlc21UZmRNSUJXOXlVUXBvOHEzWEo0PQ=="\
           ,'台中市大肚區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/5ae3f2c8c33a9b2383f4b84e8abca8c2?q=VTJGc2RHVmtYMThHZmpTUWRGTnZOR1hJZG5ONzhlL2lWWlZEdUUrV3l0M3JCTHluVm9vT09lWXlUeWxwUUFxeXFFQVoyNlJFWCt5bWVjbEhXeW8zeERYOG5aQ1Z2UmlSdWRqenVZdHprc0FHNDRnSEo4N1p1N3ZqSDRtZHp0cVVZRFpONThIbW1HdE1pV3dFdHRpRmlwbHBGUDF1TmZ3NnJsQkl5TFREZHFLb0ViUVlvZnh3OVNkYjh1ZTVsckJodVB3enVmcHgwRmZCZi9NVjFxYktVMlF1bHk3YmtiY042Y1JHV2NEalFoN2puQllSZHowU1l5dVdiVWJQT1haK2plZ0ZnS3g0YmV6REduYlY5Rk5ROWhMVlhqYnVSdHRWbzgySjVuN0tneUQxR1RaZTFpemhlMmFxNUVubFkrM2duVnB4YVNZM3RIeksxUTlHVUJXQUFFdWVaYW1lVEdSR21RR1ZPYWRCbEtmRDJnbkpQcVF6Q1dMeFVwamNFbjJLdXQxa2g4VmgzNmV6VnZQMUV0WDJJZDNSM3N6Q09rUVJpZzlyWEpTbUIyUFN0TlZuMENtK01zQlhvR3B2R3FhZXRnQnFVeUlnbmlQVXIvdGFvZENobGFTL1N0RUlhV1lKNCtkSU1GcDB1b3RRd0VienVYcG1wOTF4eFNOQUIrVWRicWMwOWFIaHlEazR6ajkxRmRwSThCZGg0Y0pqQ0NmYUVYWHhFNEJVeURRPQ=="\
           ,'台中市大里區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/c3e6702f11bef642a3eb779935697792?q=VTJGc2RHVmtYMTlNU2UwSTRPWkl0REJLYTYreWJLY3N4NlJ1UklaQVk3Q2NtZ1pCSlhLSVpNNlpIN2REZTlabWJLYkNpdzRQamFsS2dWdGtCK1F2dkllSnMrTHNzUzdkMHBSbTU2RUpaQVEyR3RSR2tBc3l0MDJERGUwa3dnS0Q4eXFJbCtqbTdPc0szREpMMmg2S1VNVnBxZlJQQkZNT3oyU3R5UVAvSVhjaDNpYVZBV3IzVklrSHVtcUxPMlpqK3B3OXdhcVMrL0l6RUJIUDI4YzVMUXpTT05aQXhFTUdzbm1iS0J1ZVJvN2RzeTlRZzN2QjVjWHJUTUoxMlVValZXanM5QTBJaDBUMUdYNm1hUlpDUDVySXY2Q2hxdUVHaWp3T2JaZC84NDZnRHV0ZCtHUlZoV0ZtQ3NzanphNlNpRG8vaWQ4NXNsQ21pYVFjeUVSZnNiUEhnSUp6MTFUWVpvV0Q4NldtQnFtVFFUUTR6c1QvcUtHMlBldUVpNmdyRHcrOHN5S3dGMEdud01uNzVWUFBPNWFQTENyTklaSWRsOGdKOXZTUGNObWFad3k2WjN6SU9Dc1g0ZGViMnVuR0Qramc1TUFPS2Z3anhOVmZuSm1NRlA1SDNWR0VVV0kxalU1bmN2bjR3bnRQTWJZRWk4cC84MXhWckxaNUpLNVREcFRaTmt5Z0VxUkdHNVhzekdITHd4cTJOcWI4UmIzRUQzQjg2Y2Z1WVdzPQ=="\
           ,'台中市大雅區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/aa376e62d715e1d5483f1023419fd155?q=VTJGc2RHVmtYMSszTmdEWGpPcG43eDQvTnVOV3UweThNOU1LQThod29kbjdOZUIxUURXWFlVMzBjckVSQnordWpMdUlQTzYxNWRVdWRzMzRmalVORmFEWk1VY1lQZWtCd3oydHFDcnBPdTRXaThxck8zd0N6Y3IrY3FLNGdjK2M2MmJaRzV4UUR2M2xYek44VzNsVGhzQTl0UEx4Q2dJQitPd0h4QWlJVnQ4eTF1MGJlK01pMURhY3BtTmhZYUp2dXluTWRQdXg2ajRyUVQxbnN4NjJzUHpzUjNlZm9vQUJXb0I3MmZGcGdzRmxML2ZQcnR5Z1pwT25LTkxLTTdBd284VnRpeHVBbjEzcUJSbjFsekw3ei9VdjVwWWttWm9WTE92Y3orWWFOaEsxZmFUMVNFdStRQjZ1V09RUnlTdnNzZmJyVjdBK3JCMjk0ejdWVXFxWDJUZ0t1QjBMcmR3a0E3STZoNUVqY2ovT2dTRXNPYXJWTGZSNUo0eUF1SklTRXJSbEgxU3ljQW1vVjlZb3RxeUxuVEV4bHowMEwvWTQ0ZXp0Q1dMeExiTlcrWUFKTjJRcHlrN3lBNFV2cE53YkdtWlgwdENJZ01EQkQ5L3k2QVdtYk03Vm9sYkJ0UjhYRFAzQ3Q2eThpVHlQNXo2NmpGbEwrRzV3emlQVU1PcVp6QWZHUFlMYmJtYzRoZHAyTEhrY21KRXlYakNhM1NvSU1DN2txSDMxTWlBPQ=="\
           ,'台中市中區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/9c0759cb9da78af0ed7d830632e7a7c5?q=VTJGc2RHVmtYMTgwU1FZa1ZCZUQ5ekpJNkltSGw2bDRpMUNHemhkNXE5dXREbDlUaXo2V3hZZG1icUtRS0dMK0JEMDRrT1FtTUxQcVh4em1JZTNpUlBjTFZCM0FrY1VJQ2ZIS0dCSzZRd2EwNG1qb2ZsQStyZE4weWVYL2xkUDR1cGZJYjMyZU1HR296QXorby92d1lGUEsza25LbHBySXV3N0h5cFE5YmF5RG9JVHVHTGc4OEIxbTZZMGJKcmN4akpZb2hGWGJhV1EwRGhQeUpQTU41VFY0VkxCRXI1SWQ3STZlSWowL0Ywb1VRbTMxd2hHVHYvYklDV05hYitIYThIRWs1UEhML0x5WXFPcnAyWEVjeXZUUjdXcGN3QjVycnJ5UzJVUFZKOWRpQmMrMWdTTHdYTStHRmFERHA0QUwyVFY3M05Md2xzT3gzUmQwVzN4a1F3THRJV1VtUUJQeWNGTXpQeUQzY2lzcC9HTmpGREVSY2NIL0g3azdqMHRzRGNadEd0OG1OWWMrOHVxNzEybnVSVTRCckdkQzdkUDh0TVp4RkNmeTZOS1F3MEdNbzB4UlZ3YjF3MW4xbzFraVdkb1lsTE1mY3N4MjNZSjc3dmxtRy9WK1plMERPOXMvWDk4Yy9CYlpPM1ZOcHd0a2RtbWhqeUQzcFFCYWJvZ1BMNUNFM2xwU0lJaHlMK2hvanBzSVZPcjZnRmYxRXQ3OGtqSFJPakpkZWtFPQ=="\
           ,'台中市太平區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/357055d57aee72ab014dcef0fa9c6fe1?q=VTJGc2RHVmtYMTl1RytxTW5nUk0zdGROQnhxcTd3NmFLSzBIdDY5akk2aklRL2Nac3VUYmtKdEFHVFQ2TkswRXdrRlo3MXVYWkVrN1o1TTJhRXFyemFyQ3ZYbXBydVY3SmttZlNOcHdRNmk2L1Z3eXIwSzJiOWxqM29UaXlJQURuVUNTTXpFVDRRVjR5Q2ZKTUhLWmdzUWdPOW5pbWZsbFRIN3pTaVJZcmJHbjlPL0NwL095SGRtVXloWmoxOFZDTm40bHBUMExkWEVqaE1nRG01R01vRHRRZHBCcGRFKzhBK055NEJpc3ljcjMwa3VYZnF5eFlKSVJHTlFzSWtwaEx1L3grZEVnT1dzVG45VjA3Mi8vR1kzT3JvRWtSM2tJOUVLcHpXSWdmdThjeks1VGtidDZtT2dzMVJYT3hNRURUV2djZHNXcU13ZFVnaDFaVEdwY0JQNmV0V1kxbmlESTNmRHNGNjBVNUlQQ3BBdnNKaHFzeHlFT0V5WnV2c2wvK0VjeGFDNi9vcXdkRGp0L0t0QnZqYUZLTFQraEw0OEVWY2RRM2JsUDBNNUxQbkJKUCtYaDJJNHBQSjl4RlJpM0t0NW1WczBNVmtqMXpPazk4NUxLZlNvOUE5dldOQ3Vvd0ZZM0Ftc2Q4bzd0aVd4NWhSaWpIakc0Um93ZlNGRU5pSlkzbG16c3VFNHhKSmx2RnFWb0ZpUGVmS0hoTUVpZVp3VFpnU1NwMUFnPQ=="\
           ,'台中市北屯區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/f01d5d64fe93cedd38eed851a31519bc?q=VTJGc2RHVmtYMTl5RUo0NFQvTkJVeUNONHY0RkdTbWxBNlZpUHFITXdjdFduN3A5dDlBVzU2VDZFK3FZSnl6dHZIVXVnOEtqaXFqNXE1WUk2VG9ZczhmNklrZFNvVk14TzhFSElnWVdJR0hXcVkwWmxhMUVEYWZXOG5TTHZUWTVLWTZsVWs0OHN2Y2czb2RLd2xadWRxVWcvTk9ZQ2J2N3lMa2xzampvd1VPdWh0eEw0VTBsUjNZcDRjMmF2VWVzU3dmRUhjdnI3WDlsSVNyd0tUSmMwM1pvS1RuUHpNNVE0R0FRRTI2YTdzcnJoeHJxcVRobFJYV05FTUZDYmVTVitLUUcrUEZPWDlOSlRybGpnM2xmODRCVEF1YnFFME9lemhNL3FGR2NMSXJGemFXNk1QZWJ0VnlPSGNGbFg3QWZhbzZpS3FGR3ZQZUZUTXBndFZRM3JiZ0JldUR3UkRXcGsxcUVmTWFDZVJya2hCcHk5b2IwVVZaM1JEQ1NGa0tkWnFYN2NRWm9uTVhyYStyb2Qza3RLWHgreXNjUzFmUWYxVVBoSEd1OCt3OGdYRlpwR1grV2VsK1R2eEIvREdzb01zdllFTzVENHR3a081RWpkYmNuazQvQXFycnZ6UDZlczlwQ05yeStVc05tK1JKMS9FZmZHdFlvWWlXZVRoN3hSakdEQ1NnaS9najJjaEMwanJhNG81L1RYcjg3d2lGTzFTd1JFOEZrMlhvPQ=="\
           ,'台中市北區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/54308d2c92ac5ba7a5792ea06ab164d0?q=VTJGc2RHVmtYMS80dkMvWUozaHBjKzdSTGR1bVluc2pKeFZYMXMxNXl3dmh0U2tPSXM3Y202a2k4VzA3N3pLaUN0anJJQmdWWmZxYjQ4eTBCd0wyQ3JKQmI5YXBJdi9vVTlXVnR6QUZQMGU3cHBoVm9SY2ZqVFdKb2Z6dlZ2SG02Wko4blA1Si9tMmowczJSKzZmQld3dGY0cGVuWU1rbk1iTmQxME1ONUpYMDBOQWMwR2JzcC9VR3JWQ25SbEdqL3g2aDZNLzk1VmVXTlJCUEV5NUtHazhRVEhXNXhiU1A0V2JTTHlpYmplVVc1WlVPVE0yM08zaEZvQWphL3BzSnVrR1daY2RPZlJERytVc0VKc0lhQUljRjNHSnh3ZzNZSEZzaGJ0MTZKeVVqZHdwSlp0T2xNRkJEekFJVDYxYS8xMC9oM0JTeDcrWTRaUXRhbDRWZGtObFNxQUYrV3N2SGM1UnMwQm9ZMlB4MlpiNEJQTmZnd1BNalhyN004c2FnNFF6ZXNScXRmNEJTbTlyS0NuMTR5eTdpbW1BeUlOWFQrWnA3UHgzS2V1eUFwZC82QStZRmpjTGFoNEFlekpPTkRPNkluK2orZ2FrWFZkbURxTzl5ZzBVS3JBak8raU9nSHdKUHdvcG1SMFdrbXhWc1YydHNnMGY0SVZGMmJ6c3JWZUJ3amNTUlFuTTZCcjEzamJWNEw4QStaZ0RCa2FOczZhSkdRTitMYWpvPQ=="\
           ,'台中市外埔區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/3a47a42e96ac338dc9bb78ce5fc074a1?q=VTJGc2RHVmtYMTlrWVUwQmczd1dKaUtMZFNMVXA3NVEzQzZsSHlDL0xmcis5NkpQQjYvYjJmei9uOHdKS294WkROS1dGL3lRL1FWbjZPYUtwM3NZbUY3ckdZQUErZDg0MGU5azVnT1N2WUdibVVPNkZ3UXVhUEFSWmYxY3BOYjRwU3RuVVpMNDhwaHRhc3JlbXE5emFiM3pwbUZjYjFjNjJXb2huUnFRWktUcjZ5UE1uVkFUNlFGQkVCTFNpQUVNNURQTDdrYmlYb25DMGkvUlpGOW0wYmF4bnZTVjlQK1NENzV2RmJlRWRPS3JCeW9YYnhCdGlVcllsL0JMbWkzMTJrVkFGRkJxWFJCc0JZMmhORHN4VE9wUE9pWS9xRmNxc1VxaFVsNTZWdE9reDJMOWFyTlgxQ0hYYy94Z2tmU2JSMjdRZUZFNkZ5YVIxY040RjJrblVManlTQUpuV2xtTTZNUjQyVk5DQ1JSS2kyZnBacXpWVWlJTnU2SlNIU1RIS2tUU3NsRDhPRXhvbG9JdUlpSVlRajhibzZzRGpyQml6RFVTbkUzY1YyZTM5WlZTTGZ3OFEvV3liMCtSVEpndGpSZ1VCdXc5MEhpdVZaWDVCMVRyQWxZdUJNanZPNisvOTJWbmQ2eHVuSlBZeXNKeEpwZGhzUE9CemNRbzVjeGxSRFduUHd5bnYwRklYVy9Nc1ZsdkVXdDZBWUhpd3dZK1NxMi9JR05UOWVFPQ=="\
           ,'台中市石岡區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/61444364e3ad6507481719e495e145e1?q=VTJGc2RHVmtYMTlGeTdKbUdnemUvdHU5ZUVxdmZnaWJFaU1HVkZnYy9KRTFxYVhLK3Bid2NoRzJJaGJibEpQYXJPSHZKaUh5UWhDbldHUDVxV04zQXE3Zy9mQUM3SzNZUktZNXd2dFYwY2lObURhcWY5V05paEFqRWk5M0dINUVLbm1IbWphMlpYNFdqMzhydmdrVGkwSGh3SndJdm1DQWZCa05HZXZaZ0VEbjNaREgwTU9QWmk5aFpxNW5zZnpZbVpuZkQvcENHRGFJMTQrb0M1aU91a0o5RGJKTFlmV1VHL3B5bnIwSFhrb1ZCWkZON0V0YkRWK1RsN0JTQ05yU3FXL2dNWEhQQkJPR05SejU5MDFuZnJXSm9nYzlhdDBiaWlFejR0cmk0V0VDeEgzZjJ1dUFRVVdhWWxJZ3ZYL01jaE1GdVNuRlRzZ0JhM2RINCtyMW1xVXAva1lLZGJPSFVUSk9pL29mRDNuNm9nNktGUjlPTEV3Q2lCM0tKaVNSS2J6UUM4amtnSlNzdTdSNE1PaUczaEhkaXV3UVU3MHNIUXpWekpselJxb2Jsb0c1ckFER2tXMmRYZlZhZ0VOS2t0eExKclMzaDl2VFlYeXhmbW9vRFFxcjJGOE5yUWVLOWlLdnRLcDdBREVFN1NaQ3pyNENia3JkalloejlLam5GdzUxSlJZc2lLQXRrMFdPQjFwUmRZVjRtQ25iZVlhL0dWaVhtUVNXRU5zPQ=="\
           ,'台中市后里區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/3e93cbcc4eb4022790c0a3424e2829d9?q=VTJGc2RHVmtYMStNYjZvNEM3aHYwMG85ZGNDbjh4Slp0Z0lqakRQd09zR3huTFEyajBFZ2JKV1RuRjhHV3g1aG9xeGsreEFUTkYzNjhPMmwzdFVWS25rVUpxNFh6anNVd3FGUVZQdjQ4Nm5CTXdTUE1yZ0tLZ2tmNXd4RHN6dFhMR21GeVVoWm9pZm5tUnhqK1NlOEhvZllTQUdDd3huQ25Eb05HQUc5OTVPTVl0aEtmakxmTWZEN2tGQ0Z6a1I2VnoydGJDMDhXZTV0cU9mMTV1QzRBUEY0QkxkcFdaN0Yvb0pqVldvYWxhZS9IRUVQeEYxL25Qb1NZM29aQk5jYldPSWpWZzBNWGZvRHIvTno4VnN2VGsrcEdmMGkxekE5dDdUN1NzMG1nUGROUmNGVzY4aDBiYXlyWE1WMjVuVkpZS2drY2RmRlF2S2dwQ2p4UXZUWWovK29rQnhMNlJORGoyYmk3ejN1TW5MSDdsTVJxY2tsbTlodFFQdXo1UTBDaStsVXBOdkhpemRwZWdUUkt0OG8yR2MvRGUzSmxiRzk1S2l3Qnl4c2ZaZlNtYzJrSkxtQkcwTDZkcDlVd3k0SUJPYmQ2THJ4ZER0eG5KZTg1UDBBS2FKbm1aWHl0Qm52ek9idUo1NWt1M25mRGV1dU8zTjJyQVVtKzU0NDNyVWRtd1M2dnVoN1V2bjkwa2ZTYTcwL2o5T0Z4SDlZbXlCYmo3Z01QSXZnYVNJPQ=="\
           ,'台中市西屯區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/d58e6346ba9624cfb743cdf97d5da5d4?q=VTJGc2RHVmtYMThwWm5SaUs0RzN3Z3cyT1p0a05tWVZISFNXaDE5OEdaWHpGOEpTNnRic2JjcEVQekhNaDZOREszczdKR0dRTlZKaHBLbDRmUWxCVWNxQXk0K01rSzh5RTJlRFB6a2srby9OUWdza1BxbWZkOW41eW10YlZxRURZcDdkc3JkUUpNY1J5TVpWLzN4bDdpQVVRZlMvMXM3RUptcjlDWm9RMHRlRmRiMW04SWx2T05udDBTdWV2L04yL2ROcFZTMFBnT3J2eVlkdVBOaVhZUmhMVHFoMG1VSzFJRGNEOEszdFY5dGs4Y2E3TkZpcnlIYUFaMjZLWG9tcktYaXRiL2RadEFybmhhcy9xU3QwdkJKbEJCaGIzY3MrVHVuK1Z6ZWo1NzJic2ttVXcyZ2ppNDIyWExtRDFHM005VEMrNm5pUXVSa2UrdHNZTWQ3WTNGTDRtNzJ0R09ZcXo0OTlmQ0V0WVdTTGpZSGpFSnlSdTQ2N0ExZGh1VjlBd0pkb1dGMWhGaUhkSjdYWmlyOE5JN1I0dC92NWZ0OHA3RG5tMnFUR0FhSnY4anZJaUdTZ0NIYVd5Vk12SVhvMXRqOHVDOWRPc3p1Zm1tc0VzdTlrY0sydFI5cGxNZjBJTXBSWDZjU21DbXJTZ3Q0dTdLTTh6clRESElhRVdndVFFYUgwMUJuRWQxazFrYlh6RUdWVitlcEhBQ0IrZFFnSzU2d3lHOHdTQlhzPQ=="\
           ,'台中市西區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/d9864af4ca7504c9f2cfbf617b24762d?q=VTJGc2RHVmtYMTljdVdnL0xERitUTDhFN0lIOEVSUDE0UDNjRGlSSS9uN3FpSDJvenRJUERZZExMRVM5OXZoa1o2NnVFNU1xT3F2SitSZjVhTGpoaUNHTTY1Z1IwTTBFVkttVWFRTXJqa1V0T292cXBIMlpCbVBUNk9DN2czTmE4Rzl6dW02RWdybnc1ZkM1OHZjbW4vbUhJOEtpYUw3VVpCYTNkdUNSUE44bEdMd3RrajQyOXBoUlQxOVpTMFptNnVqc1hKN00xRmVVZUtQNE5pc1Q4TFJYT291ZGNJTFhuc1FDNTkyb2Q5Wm1xNWh1M0V5VitkRVJwaU03Tm1qKzROREVTaTc1WFJrNXlNc1JRd2xhZW1JWDk3QzRFOFRDNjNnM3FyMHVLWTAxTXNIMnUrYU5ZZ3pVRThSR2hzS3FlUkRxQVFvL1pQd2c0d0ppMHltTTVIQ0NxTHZzTHBWRS9YSlhjY1AweHdoWFFvMjViQUJjOWZEczZEMklSS3hDQXBoRHRxVFV6Q3RSc05wZktRMGZ5SjJvcEF6bXJ0b2NDNlBBWXdqVVpublRnZWJ6TU5LaGZjSFJxdzF3Wm83VjhwdmZLOUFHQ3d0bit2bkl2OCtSajZmUlhqaWlyN3BuS2VIZmdlWkx0aVEzdmIxQjBtdFo3SHIwNXAzejJYMndoSi9GRkh0aU5lZlVJbEFCWFZpVUJ5SGhoVjhMdTNPK0lyYzk4a0J6WEFnPQ=="\
           ,'台中市沙鹿區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/1a09502373c9943ec5e43d7503597f92?q=VTJGc2RHVmtYMS9YR1FKd1EzUjRXYmZyOUduencxeENsL0gybzYreGl0VUZLR2VhRXhwSkVHM0J3bGJNK0hRanZFWDJPang3eHI4aHNNb2FZQlZMU3FjaTRVczdXcUNBcGk1ZngralpDR1VIcEsxK1ZPNUZMejRuS1lGZ0lTSXN5NW9yVlRISVFJWURNSDFBcGRNM2pRN0pYYWpHQndhVHRmajErOE5aVzR2aXJtZWlwM2F4bEhueTc1K3Q2VFNLdmN0dUNHK1VLSkVWbkVPOFNKTTVXYm5wQUNYRU1YQUtRdjJpTlhSUTVRdktzVHEwMURlQWVtQ0lLV3Z4SVJ2TTc0eGVLZDdCcE5OcE0rVndObUV2MmxtMDBiWlJaWGpVUkhIc05kc2xBa3B0YzJmdFBVMjUxWllQOHJieVlRSkF5a0xPMXg1bjMxN0dDNVVaeFE5MDhzZFZFZFJFQ2tkMlhWekg0LzhYVzhGUG45YUdEWFBhMUhuMmUvaVMxcEtZNWd1Ni9LNmQzTHZvZDhhVE1rU1NROHE4THd4QVFxTytpTVpkS2JmWUVEbHZuRy9jWnR5SXNlMDJHY2d6MGZQb0F5bVRtNWl6RUtUTVRwZjNoQ2pSR1hROVRvbFkyQm5kQ1djQ1cramFNSkZvWmRHS2ZodTFKYklHdUpKZUJDNzlIUGlDWFRmUU54ZHVFSHFrT1FOeFhDeHliazE3eEJacGZya2Y0NFdxRy8wPQ=="\
           ,'台中市和平區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/8bb1e688746e5834fcc66fa83d954251?q=VTJGc2RHVmtYMThYMzJJWFpFVWtmYStpL0JXOUtpSjB6QWw3MUhZcmhzVnFWU3hjQndlTk54MHU3UVZNdFZWN0ZMS0xCcDkyNDRQVDYzQ2J2TDNUanpHdko0M3RtZEkwdnZmaHo5MGRYL0xaWEQ0WW1yYTR0NElibktzQ1JNNTRoN1RPYThnQnBIL0RaK2RtOUFxRjFXQTJVcXpDVW5KY05FUW83TWduSU9FWlN4c3JxZzJ2NDVaYXBzRW1tMG1ibE5ySi9nU0VYc2RySFk5OFIwMDlGN2RwdCtnUkpWcDg5cUhUdGE5a2txRnlTYStwUWRTT2RBWUlhNEZOc2p2L1QzaFlDL3ZCcmhJbWhaOWFtdjFXRE5uWHAzRzF4YWN3VXU0WHlDRkV3bnlLUWdiWnh5Q2tSSDJqdjEranBtYlZjRk9XZFNlYUFkR21QcmpzT3dzRTBId25iWmdUN2NZYkpxM1lBRlZKNm9xVUZCT09qc0FMWlFsc3FOY0tHRTAyM01wenQrRjBLRzZVeU54U0lqMG9ReHhYcE84YVNpUkFUUmxQUGNsRjh3ZVU2dmYrYzVrUGxkTXY3OXA2M05CRFpJSnJ5RXlyTGt1bENMSzJCeVY5dG85Q2RlQ0NVNUdKMXhaWXpnT3c2V1BnUkpGZnN3YlBIZUM5WTZsYUpydHpra3FwY0dlZklLb25CcHppY3JBYWZDOU5MZzljSTRnNUpFTG9CSTFwdkt3PQ=="\
           ,'台中市東區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/576e6fe1720c94918019cf7b712ab8c4?q=VTJGc2RHVmtYMTlhNUtudHFJTEpDR2RxZHdLWHE5WTA1SVpFNU9URm1tMkcyY1l4UVl3bHBnbmpXMjdiMThRS1J1bXJIZ2RxVHhvbjNZQXl3aUxFa3E4Nk11Wm1xcU1IamhHa2VaUWNVcGtEQjQwZkxaSGNkaEpiRWxLNTk3SGJ3U2xiY2hmRG1oaDJmT1FlM21Hd0xFZGo3U3duN0dtTUNIQVVxWEZuZy80Q21GVDZDRlhUVFJtelNkZUpTdHJ0Tm9hMDN1M0d4L2JtM2N4TDhaeEwyUVhKZm9kV0ZNOTV6RWptZHZucTYzejJ5T1JQZVFFa2ZkVm9YTzl5YnkzSW8vMzB0dmg3SUkxLzMxRkFPSXBQQTVBdnIxM0tQNDhvcElnbkgzdGpQR2J0dXF4QnExREVFaDNoSTJwTEs4ekJsenVjUFNtblhTek1lOC95akhka09mUUJIckUyN3hXZjZFd0pQR3R2TVErWXN6RXJtQm9DVU04THFlQ2FaQjRkMHFBcUk3TFh6cUd4QldrbmlUNWRVZW5JbWxjQTEva2hVaU9CcEEwa3M5eWtTbmg1ckswbW1HaVpKSEQvbkJNSUJGclF0cEdxYTJrVXRLNjJlYUkzMFRWQ0cvbVE2aEpmdjNFWWN1eWZ6WmV0MEpnUkZUbTgwQUhEanN4d3FYcktGVWRQZU5QbzhYMk4zOUREMjc2RHJzYnRQcDZ6K1phcjZHc1RrVHpHMU8wPQ=="\
           ,'台中市東勢區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/57babb8b7155879c79da32615aff931c?q=VTJGc2RHVmtYMTlrK2pQZEt6M21tcTlkSUVucHBFUnpqWStQUkhHSkovNURXMVVhd05MSVRtL3AyTEZIYzNKUHkvUUF0KzF1RzNaaGJPZHJhRzVYa2lPOThlanFEdEFCaDZCa3dIYnhHVm5Dc3hZdU4wNnBpNWFsMVVuR2YvUVUwdVI2V2lZRU5lR0wzZk53RWUxb0hXeE96a1N5VHU0YWpkb0x3MnJjeUFsY0VlUW5XeUo3aE5YUDJmZU4xZHR6Uk9ocDBnUDZlellHeHRlSSsyczdobkt2Vk84azUyaGtoREhqUWxGU1lLSTZpQ1RMbGJ5bS9CbUNYZzNTYm54clVRaXh0azhZdHY1clJFSlF3bzk5aU50bWtJMmpGbnNTYjJRQmRrYnRKczRBYXJJRE12bmxMYWFPaG1nS3E1bXIyN2dwR3U0emVaNEhUYjB3cVRaWTZJcXZBNHJpVDN5dXNuVjB0MW1XNEFBVmpFVjE3UWNrQW5VemR6WkZtNWt4NlU2ZlNXMFdmaXFXOTRWeEticFVJTzU5M0NYamJmOWVsWTdJMmt0VXdvc053YXJJWnQ1QVI2cTVnSERoNDVMeG04UFZKdUJXbGVLL1pTc0NqdFI5ZUF6QXlrRGxEZU13R3crVGRJNk12MkljNjBIUm1mMlJoTnlsRWpFbWY1L0VLd21VZ2xvUlFwRTcwU0l4RVJ2MHd1allLdVBPZXE2Z3B2NEl6K3l3MG0wPQ=="\
           ,'台中市南屯區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/fe3b32869e8a04ed3d3fb99aa97e0fd8?q=VTJGc2RHVmtYMTljTU9kNHpoR3dNTXNjM0szbHpyKzNuSFhZd2hKOHJwMFFUMjNFalBlK1ZmRmcwdWdoNmhFQVMrMUdQcVFVQWhuWmVLblozay9JY0Zkb0xIbGZyY3A1NUt3UVVmZkRpcVJEWGpTNmliZEZhV21HaURZVXVXWjVIZWtrVnJCaHdvMzhEditNTmFHUzNBSGorK1RjRGtQTFh6d2xtQTZUL1hkV2lJdy9oVXptVEk2NkJGLzYrdDQ5aXg2TjhPa1JpcUVOVmladXdiYWpQSEU4T0NqUmxBdXRHZkV5SXdBWGdpMUJnRVVlMEt0TWVvVEVkR09FZXArbE9uYUZlcGJYQXNuZ28rck5VVUR1SkYvRHVDWDBZc1ozMHRvM2xhRktpTUVsWXh0VVNYWmN1OU53YW8rY0JNdUM1UDBFaDZ5OXdmSHlRUnZvbW5XWmRsekFKZW9jQ295eHpiKzhaNGxtYTh2MldIK1NrdjEyL0VxdHV0MXFhZVNhSDQ0clVaSG5Ld3JGTEIzT2xmUEZyMUhOMVl2TzBETENEVHF3bkxSNi9mNlMzTHBacmM4U1VFUWYvYjFaUVlTbVBwNWN6alJRcGJPRE4yZ2dKOGZOMDViRnZCSkRFNWsxdGcxditmeHFmbDNtSVdLbUgrWCtFcXdENW1XdmNSUVE2dmh1NEk3Y1FUd1kxNzdqYkNzU3VZWHJLc3I0UVVxeHBjZDY3WW9vcklJPQ=="\
           ,'台中市南區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/df40794cee9db021f669fab9b740d3ba?q=VTJGc2RHVmtYMS8zeWtmb0s0bk16am5XcEpMMERzdEVLeng5RWV1bml2U3FrcFJidUVnRFRxWXhUTTJ6SC9URXBpMmR4cnV3Nkh3M0IzRXBRdTVOSlkzZzErblMwdjBZa0tkaXUrTnk4enhYS1B0N1dHY1pneVIwRFUvZlZqbDVOYXM1QlZKNUZBb1AzVjU4V0VncE9yVDE2ck4zL2R0RlE4Q1lDMkZvUGdvbXV2MWkyeGd6bDlYdzQzL29UN25jNVFTL2QwL25va284Y3luaEE1VmNPYWpiTUFQSHNqYzF0WE1ENHZFRHYwTWJ0djlWZDcrbVFKTkNLRGFqckRBV0ZPcWIyZUkrM21TWmhlU3lyYjF4R0Fsd1pxYmlBUnRXOFZmZVVDQTFUaEQzT2gwTnFFUnNablhSekpqeWpYZXluWkFtOFFzR2FOenFKRnB5b1dpd2ZhTEt1NnQ2dkp4cDBCWlJtTy9yMUZ6ODQrUzMra1QzUWRrMjkveTloZ1JpZk9vejZIVHNabEhNT0g0aFg3aFplNk84elc2aTRUb1N2dmlWK0U5KzhManpmekEwRnpzYXNseUlwUklaaHdnM3daTmphaWRUN1JaeURWcURkYUtwdGp3V01ucUVXZTBobDcxTnlUNWZ4ckQ0eldGR0g0NlJkclFkVzZ6aVNrQ1lsR0xqWTRNNVRLQkU5SFBMN1JjZitSSnd3NERMUUIvTElzTzkrTFhVdzlnPQ=="\
           ,'台中市烏日區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/2cca336ff65f6579a9a01b0a06c420b4?q=VTJGc2RHVmtYMStNZTRlWEdJTVVoVkNMeXMwUUU2UG9vR293cWxaVjhESU1YMmZlUG9ya1U1VU10TjZzQWhma1hMRzlEa0I0R1ZLZDc5RkxLZDVqUzVZQnQvdUV4aXNpRndYSE5NZjJEUjdhTFRUK0oyUlppc2IyaVRxamdRY1ZDZmZmNk4xRytacUpqRjJnUFl2QnRhZ3lRZXpuSy9vZm1DdTM5ZytHWTVzaHNqd3A1c21OcUN2Q2RKejFkaDFzOW41TmJZbHhlcDcyK2tsWHNrUnh4cFJWakE3QnFqbmxST29HQ3JZOW0xRVhoa2xhUTFiMUplaWNqVkE4eDVRZi9sZjdkNzRZWmNQSGk1WHV2NkN6ZTd1eHN1YUp1UVhpdFphL2U4YTV5aFYyV3lTejVCSzF2WUFteDdyRnovV2k2MFdleUpOd051YlN3UDR4Q0FRTDhKWUgwVDFmU25zNzczUEp3TThXSXRWWFRNeURxWXc0TE5SVHovZFM4QWx4Z1E5cmxNc2I3ZXNiUDUwMzR1YWJGTmllbDI4bXVSTk1VWEh1WkhVU2c2em00eCtneTBMMkZNSHp6eFhxVHMrTWFCd2RCK042SmdhREt4K2FxS2hHZ2pjYUpOUlUzSTdLbUF5S0lJNTZQWGxxRE1mdmd4TWxnRzdacmpoSFY2ZUNkRkUzakY3Y0l4bEFtN1Y1c3ZCWmUxTnBxbmZOY3l4QTRsSXNic1RaaXg4PQ=="\
           ,'台中市神岡區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/7aa3e55cea5340cabfd147a6bec2bbeb?q=VTJGc2RHVmtYMS9ySjd3UEVTbnhtSXo0cVU1NkNJVXhQWVlkUlhWdXdlaUhIY29zMWx0YUtYeWJCOGtaazN0MGI4b3Z5cWFRU2JkVGxPL3ROdVVGTGpLTTlYN2V0WWtkWDlUUzhMTUhGMkNpUlp1NmEvUEJobjZiWStlSnF0Q3d3MXBLYjFaUHdBa0ZoNGRMMjFWQWV3QS9LS3Z1VnBDMU9va3FnYnpOeGpsRXlIVTU4VFJQdDhIWjQzay9qNzNPaEJmdnZqUmZ2ZW15SXkwRVJUVW1pbGdTZVk2VU9FbEhheFA1dzhTdVpwM3VpSWRFcll1M1g0NDJGdHdxZTJkMFhiMjl4Z29iVkFKZFptNG9YQUx3R0FJeEJ5aHdjMVFrMmNidDQrSGNQNEFKV1BVMGg3QlgzVlo4ZDNmdlZnNWdXMmlHZWZVdXQ0eFRKYkdDblBUeUxPM09rZDBpbjkzSGFLUVZ1NFpWTHJXTktpY2d1N2dEV0o1eC94V2d2RlpaMHRzU3o5YkNSSlVGNnUyN0FOWnp3UVBxb21IR1JUdVVxbGVsRXU1OE5hUU8vRkgwVk5wOFhPRXpmYjFScEcxaVlBYlNXN25uR2hJQVVmRUhMczA4OGg3TVViblhWOXI5Uk51d3lXMW1FdTRXeXZjV01tSUdlQTdSSjl6MWlNRWFNNlJNMGxtUDNxUmorYklhb3ZRWDAySzZTRUxHMEV6TTdETmNrUDBpTEk4PQ=="\
           ,'台中市梧棲區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/da15b151ffe16078aa0b02ccc7d1c1b7?q=VTJGc2RHVmtYMTkzd0RCMWYwNGV6L2dDR2lobE1pRnMyT2NlQXZpZHFsYTJKVkhEek1wUDdNWjBlQ2Z5MzQrT3NtY0xqSUpqakJpSVFwZTlMNzZMM2FybDArbXFrUitBOHhaWFJjaXNJVGxYdUxoT3l0Zk1BclRFejQzYkNqSGthdjJmSWxuNE0wYldlSno3QnRySUlNV0RiR3lHNlpJdzdZTDhhMGNXVUs3TG1yK0V2LzFLdUNaek1YQkVseGlFZHBjL2RYU1IydjRsdy9IL05VV0FZcFQ1dWUvNmE5akhzWWtXdXlRb0E3TFcrY3hVK0Nmc05uRDM1dFNhaTJ2RjV0K21nSXZ6R1ZwNmhhdFpkeUovTENVNWZpdWhWbkl3Zk03OXlpcDJsZjFkMzVqK2p4V2g1TkYyOEQ5TkpORWpVNldQbEhnYjhrQzZ1SmNLaWxSc3VhNlBDN1BkWTEwc1RmbnJVWHY1cHhRdjVvTnNPT3B1UlFRNHdSZWZTT2UyR1F4U3RmdWxOVS9vUGp6VXdSeG9HV2o4RzFJQ0tFRnVXYVBzT1dQR3RvbzAxczAvOHdqTTdROEZFdG5GeFNuMGd2eTlPelZ1NXZuNjJhWlZlRjNicTRQS1BPZi9JTjhRcUtsT0NQZ0F0MXpld0laSTFwYnpNMEM1QWE1Umc2Q2JvcU0ydTF6a0xCUHUzQzlJa1ZiU01GOURFY3VsMmwrZHpEREl6akYwV0MwPQ=="\
           ,'台中市清水區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/7ce123f6115f62aea49cdece4672c86f?q=VTJGc2RHVmtYMTlpL3l6ZnlhcVZHOENQSGhhWGV1ckR4TnFMZVF4Sm5QbGExOWZ2dEt2aGYwWEQ5dEN6SnQ3N2VFSjZhK1Q3eFZRSVNCcVVBQVdHbUh5Mnh2VXZlWXpHVFZwUFo2V0Jrdjd0ODhxSmlFd0VBTkpEUml6Um5wWlFKNDdrU3FieUh5ZzhiZ0NzRXhWYVVGcng4WU4wdlhqRU9MTmhYaUsvM3o5UnNkM3lveTVIWUJ3ZUEwbWlJNWdHaDJaUmtyZWlQSWFSa0lCTFdEMWY2eExmcXk5bGtHREt0OWxWQWl1OGxsOGY0eU0xTENoUjFEblBzbjFJeHo4b2I3Y29rdzcwTjVYTkFLUXZQU2h5NGFVMFkyNTRaM2hhZlp1RGZaRlFoZU9kNlFFVXkvb1h3V0MrdDBQQWJLTmFETkN1dFlsZjJ5SVloY0w5YTArNmFTRjhCTk5PR0hKcDBsK05GcDdUMDNiVEtjMERDNGNkWjc2T1kzVDJ1OVRsU3BJdHZFRkg0Z0FzZnlQZHNYQTV4QkFqUmNZYU9pU3A1RThud2YzYWhtOFBaNGlvekNuSnJ6WFlEKzJaVHZCMzROejMwdUdwME50eWZZK3lZQW1EaWZWMmNsRWwxeVUzMXBFUUJiOVJLQTY1d2dyRmpLQWVTMklPTkFuT3IrcEU0ZjB3UlBXNVB4NkdaZCtzOXgxcFlMbVIrQVZoazMwYThWcU9ZY0VYbUx3PQ=="\
           ,'台中市新社區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/241b88932b22c4c4bb283f731cb6f0bb?q=VTJGc2RHVmtYMSt4ZzFya3UxTUdja1d3OXlmSndOWXRDZU9vdnowWkt2ZW1oV0tBRnFjbjgvbFpiTStabS81QXd5OTlaRnAxN1pJU1BVeTVQVE5aSldScFhLZ3JTSkE2WkY2b09JcjZ5M0h6RzRQUHQwOVVocTF4ekNUWldac2hrVFFZSWs2aGkyeTU2d0lXWFptTDViZnlXTUxCRlVtT0ZWUHc2U1lMaVlPTVMzVGlkVlRTVFlJaVpSSVIwWkppRFFsbGoyRld3K09XVmJiM2syWktvM1VCYzFvRDF6MXlKbUVzM3ppREVXcEIxR0Q4a3VIbkN3R3o5cytUNHA2K2JQSnAwNFU2cUJzS2JFRVltaGhZdEczck1VdnlqWjRYWGtXa0ZHaHJHSXQzVUx2aUtXM2FKbGtpMkdQZnFnYWNyUFlFMGZqSEhuVEQrMFIzbkhmV202V1hSclBBNFkyTzF3V1FpSHV4VzVHZXNBTiszNkdVaFg2cUJWekRQM216R0Q5cTQ5KzdnNEhENWFvQTFrYjdlcU03RjNnMVlEZHdVRUI4WXJ0ZS8rdTVKZkhpaU5QS2dkWHJMRFVPZUJoRDR0MnVxdFY2N2RuaDlHV2l5MCtIejNTeGhtdGs0NlFqNWFUN0NwcU9SK1VRSm1wZFFiUDRWbmh1NEllcHAvTkJydHdyekNVYkFpckpLUzF2YWZUWmtqTDNPS21MendBZzNCOG9UWUxhRW5ZPQ=="\
           ,'台中市潭子區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/da107de1ae0e05b83829785b652f53dc?q=VTJGc2RHVmtYMStMRmRIR2JhWWxibWkyWG03U0k0U2Z4VFlCanFCU091clRXQUJYSC9aTHlKTmxoNGUxYmd4dDRaNXhubS9kWnpkaXZITVJqYU1UTGpuTk5pbGd2aFA2ek90N2tsMVJzelJxdEswNDIwUCs2TVpJYUZpMDdudDRoTnljbUFMdVRFeGxvZnZveXZ0QzgycUFScEZYU1drTk9xaE9Xc2wwSzRXb1JJNDZCcmZFaWNiaDYzVStrb1psYTk3VExUeHhMUDRyYVY2K3MxQXQwNGM1SDUxZk1aU1dYL21pZG51UkJ3WjhrejczWm9PMGh6VEZ1ZlFUZURYVTd6NEd3WHg4c051cm5TNVVQeDR3QWFZSS9nYUNsaEJPZ0pLazA1S0J4R3hlSTlnUVZOT05lQmljSUpxVy8yTGJnanlRT1d6alBIQkx2V3d3MERib04xMS9WK3NqUWxTKzVnck9KSHR4b1pkajRqWDVBT2hBMFdZOTJmL3lCNUxBdWdiSlhLTDB1eUpNSDlxcDFhVUNTMXBmS0ZVMGFad1lEdEhBSk5aV2ZIVlcrM0RqektDZ0FjRkVQcm5MSDBoSnFmVkV6cmdBWURMdTl1NUhhWFMvaDBqWkdJVFlEWXBUdTNmOVNYc1l0RVVHV0xJejNnRHNnOFNENTI4RnlpdXNsOGcwLzlrVkdYaEJsbERJV3VzOTk5UHNSWENuZFJOYVUzd0l5NEtlZVJrPQ=="\
           ,'台中市龍井區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/12a01481900570acc5f8fa16ece80ddf?q=VTJGc2RHVmtYMThwRGRieGpwYkk2UE5iK0phNVRPajU4ZUxHQy9SYytHbUtZWXk0SWNWWVdFb0xtVGwydVFkVjltSThLdTdzUlpxTlFuUzRHbXJLU2hGVjI4UmhRUXBNdXBFYlVYTWdGb3g0WmRjVlZrLzlXMlpEVGt5NzFTSGRSWTZNVGpGMEJ0b2JzMFVYZ3FkODArSDBwZWFwRmh6bzU0VzRjc0czY1NaV0Z3QlJZN1ZDTmJDeFlSRjZFdjJqdGRiMmNYYnZYMEs2T3RwZDdoZTg3SlVpMEU4Uy9HU2ZJS0tBZitUTHRWNWRvMFBiVE9mSC9aNkpBVTd4bjVqNmNVZTJVb0FtM0dKK3pFdG03clZDOFhqN2tHdGMzbS9kS2orRjM0RTVERU9SUVpkK3VUbkFQbTAvL3krOTZMelNQSW9GS0xlaWthbmhUWjBXQlVQaEhSaWRRY3hYVnF5bnoxYkFXbVk4aytrZ1VDV3JOK1BqZ3lhSXdydzFzUnM1UHdNcmxPQ0Vjb1BpTzVBS3ZWYVNoeFdkMFVwRy96TGlTbVEyQ2Y5emRad244VHA0V2ZzTGJVSXJacUxWYjZtNnFNbCtkN1owa3pRZ1hjZXUzOHNUWHZsdkFrcXg2dTdva3FjOFBOckZ0S0lZN3NPUDY2ODliRk92QU5OdGtjSFp0ODVZTXFrVHdQNW0vcjZEdHV0VEF5ZXpsUFdlMlRWN3FsZUpWQnFIalk0PQ=="\
           ,'台中市豐原區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/e53a7294d45a9c25feab1d6b6b0afc28?q=VTJGc2RHVmtYMTlaWklmQmZTSjRjY3pJWDhrTFlja241cDVRN3ZOTjg2bUtvcHJJQytNK2Fya2hMY3NYZG1Oa0RHSFQ1Slh3QmpKZmhSNjl2TlhXZDlmRStvSTRxT2xjd0FSYkZVa1lydC9qMUtGUEVTU043aUFuV2g0dUd4TmRiTjloZmEvYS9nSEtFazJhT3FQaVg4bVJKY2k0M2JtT1RaeGxNejhCeDZubDZKZDJEck9mQnBJYlgxUXQwQ3pXZVJpREVxakcyUERDakVWbGsvZkIzSmpYdnhtSU1sSHd5UE42eHBvM1o3dUNQZnovMEw5Z0Q0aW9QNW01bnhQSzJIbVRSaGdxeGlMakR4aGxGQXlZQVhDaXFwT3hIY2xuekZMbFdOclNZZXc3a0F0MWRoVDhJLzhUVTJmNzNILzlmelJ0WnBHa3hIbElhVjN5K25DUnljTnJoZ2xqZ1NzMnU4eTRPaGFCeTJ0cEZKeWd1VDVsYWMxZnZrNGNjbUlud1V4V2p3OFV6RnY2R3lZRE43WkNjMENHWTMvTkMrWG84cStCQU40MmVTMUtyOFFTRHB1RUpLZHJKNVdCT0hiSzJZcVNwd0lxWkt6djFBVFRPQkRUQnU1eUdvU0tsZkdBRjRSQUVjWEtRd250WVpmblRxdXMwYXJOM0lDT1BzVTJqQVc2WHgwbWx6ZngxUFVQY1gxaTdXL25DdE96ejl0emhsWG52ZjdxU1ZrPQ=="\
           ,'台中市霧峰區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/855b9e512fecbeb83dd4279fbe01de65?q=VTJGc2RHVmtYMS9ycFhiWVRYRmZXRkpPUjYxWHNYc0F1c205Y2xhalB5cmk3Y2l0a3Yrdjh2UnQrUzlvaWJUc2VkNjlLK00wQnFnUUZSaFhUUmhYT2pGUDJxeGVmRnUydExHWGx5L28rU3BleDUzQy9PVUE3NVpyeTVPTFFjc2VSazBGaVh2MlNZZ3Mxd3NNT2t5cmlBcVlWeGJ4eHJiNHJmZEZ5MkdhdkJFOWpaSTVoSXBqV09QYms1d21BcGNXRDlHbEwxVWl4MEcxWUR6UkVsQXU3VzRudTNHNjRyc3Q3bWgzL2lWVWluTzR5WXZWd2ZBUUE0QmJ1aXl3aHhvUWpqUWJFZTB3ZWNrNFRycENJaDJPcXlLbThpbjlhQ3ZkaHNYdTIrbmgweGdLNXJIMkNUeTlvL2psdUkxeHgrS3VqcnZJWlVqQ3VLejhhTkEyTEs1d1QvRkxGMXNiSTdxOHowMTB5alFMZ2dSd0daYzZqT0xhK3E3NkhJMUJUU2QzZW5VSkEzcGUzbnUycTJBZVdPR05OMmtoWE54VmRrTXJhY2NqaXY0bENEZ2xMMml0TVVEUktBT3dibWM0K0txN3NvZGRXVC9Ld3Zyc3FiYU9JNTgySUltSXdOc1ZWeFhkengxaTliUGpQVk05ZFpjM2dxcGxlZ3pWNDBzVm0xSFpadHYwbHpFRENIdm0yYWp6bDUwc2E5LzFwYXA3b29Cd1EyR2dXRkZRcEI0PQ=="\
        }
    
    
    
def getGeoCoord(API_KEY,address):
    params = {
        'key': API_KEY,
        'address': address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        result = data['results'][0]
        location = result['geometry']['location']
        return location['lat'], location['lng']
    else:
        return
wb=Workbook()
ws=wb.active
opt=webdriver.ChromeOptions()
opt.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62')
opt.add_argument("disable-blink-features=AutomationControlled")


file_name=input('輸入檔名:')
url=dict01[file_name]


#url='https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/d5e11d41d43c30db850da4a09bbe59ce?q=VTJGc2RHVmtYMS9NWEZyditJVzRJaUpHT3pEMDhJMHY1T3BjdFF5MWlMYzJPTWhlM2tzV1JBeGVkUDhxb2JXMEhwMmJFb1JzV3JIUEk5dmttMGtsTk81aW1qVUVvLzdrb3d2azJiblRGOVlaQmk0UGxTUmVSNk5RMkYxOWJZTnF0R0wxMXJBb2xnd2xpVUxBSGpncVlJSnhsRFluSG0vdEp4K09OeGFNRXFJbVV2QzMxY2dXWFplb2EzNldQbUk3WGYzWVE3SDM0bno4TTlnR2tkemxvM0JBNEVmVS9ieEpFamUrcnh4S2E1TDFyaUtLRVdXem9abEIrS1huaVhpNzQ0dkRzUmZ2ZjFVKzJHL1VPemxxbHpXQ21tbTNHUUtGcmNvbmJnenhDQ2RBWGI3K0FmclBDMXlZVWtQa3dMUDNmK3pIbnpDOWlJMTBRSVMybDJ1SENUeFA0TXllQW8rTXpoUGlkWWs3VnZoSTAyNUE0VXhxUTdLM3BXYkJDejhzMUh0Y2ZyY2VpU2pCV3l3YW8xQmVwUk5oQXViS2RJMUtxVWRTdnUrZ1hnamVySXlKa0w5alp6MTU3WDUzQzByY1dwcFRGU3FpZkdUVkhYczJ2NnB0V1gvUmVkclpTMGNxTDdGVU1rLzIyWCtHbG1TM2d0TVJSbU9CS0hsQytxejZXWlBGRGFQbytMQ0labVZmdld0dHhrUzlwa0k1SzlaelZEMnVqS0JGTWlrPQ=='
r=requests.get(url)

#el電梯 m管理組織   j土地 k建物 l車位
root_json=r.json() #roo_json 是json檔案格式
title=['address','lat','lng','orderdate','age','type','totalprice','totalarea','room','lobby','bathroom','land','build','parking','elevator','manage','TAIEX','CCI','SALARY','singleprice']
#           a     lat   lon      e        g       b         tp           s         v       v       v        j       k       l         el        m                                 p
ws.append(title)#先將excel title加入 行開始由左至右
count=0
error=0
print(f'查詢到:{len(root_json)}筆資料')
len_json=len(root_json)


for data in root_json:
           #time.sleep(0.5)
            if data['v']=='':
              
               error+=1
               print(f'共{len(root_json)}筆/{count} 筆/無資料{error}筆{file_name}')
            else:
                count+=1
                print(f'共{len(root_json)}筆/{count} 筆/無資料{error}筆{file_name}')
                course=[]
            #===============================#
                a_tmp=re.split('#', data['a'])#刪除address中有#
                course.append(f'{file_name}'+a_tmp[1])
            #===============================#    
            
        # =============================================================================
        # =============================================================================
        #         geo_tmp=getGeoCoord('AIzaSyD4SiKYm7-W1BIL24-0UspGqRTfX_QfN_A', f'{file_name}'+a_tmp[1])
        #         if geo_tmp==None:
        #              
        #              course.append('0')
        #              course.append('0')
        #         else:
        #              course.append(geo_tmp[0])
        #      
        #              course.append(geo_tmp[1])
        # =============================================================================
        # =============================================================================
            #===============================#
                course.append(data['lat'])
                course.append(data['lon'])
                course.append(data['e']) #date尚未需要做修正
            #===============================#
                if data['g']=='':
                    course.append('0')
                else:
                    course.append(data['g'])
            #===============================#
                if data['b']=='華廈(10層含以下有電梯)':
                   course.append(str(data['b']).replace('華廈(10層含以下有電梯)', '1') )
                elif data['b']=='透天厝':
                     course.append(str(data['b']).replace('透天厝', '2'))
                elif data['b']=='公寓(5樓含以下無電梯)':
                     course.append(str(data['b']).replace('公寓(5樓含以下無電梯)', '3'))
                elif data['b']=='住宅大樓(11層含以上有電梯)':
                     course.append(str(data['b']).replace('住宅大樓(11層含以上有電梯)', '4'))
                elif data['b']=='套房(1房(1廳)1衛)':
                     course.append(str(data['b']).replace('套房(1房(1廳)1衛)', '5'))
                elif data['b']=='店面（店舖)':
                     course.append(str(data['b']).replace('店面（店舖)', '6'))
                elif data['b']=='其他' or data['b']=='':
                     course.append(str(data['b']).replace('其他', '7'))
                elif data['b']=='倉庫':
                     course.append(str(data['b']).replace('倉庫', '7'))
                elif data['b']=='廠辦':
                     course.append(str(data['b']).replace('廠辦', '7'))
                elif data['b']=='工廠':
                     course.append(str(data['b']).replace('工廠', '7'))
                elif data['b']=='辦公商業大樓':
                     course.append(str(data['b']).replace('辦公商業大樓', '7'))
                elif data['b']!='':
                     course.append('7')
        #title=['address','orderdate','age','type','totalprice','singleprice','totalarea','build','lobby','bathroom']       
        #           a         e        g       b        tp            p         s                  v
           #===============================#   
                tp_tmp=str(data['tp']).replace(',', '')
                course.append(tp_tmp)
            #===============================#
               
            #===============================#    
                s_tmp=str(data['s']).replace(',','')
                course.append(s_tmp)
                v_tmp=re.split('房|衛|廳',data['v'])
                course.append(v_tmp[0])
                course.append(v_tmp[1])
                course.append(v_tmp[2])
            #===============================#
                course.append(data['j'])
                course.append(data['k'])
                course.append(data['l'])
               
                if data['el']=='有':
                    course.append('1')
                elif data['el']=='無':
                    course.append('0')
                if data['m']=='有':
                    course.append('1')
                elif data['m']=='無':
                    course.append('0')
                    
                #TAIEX 
                
                if  bool(re.match('105', str(data['e'])))==True:   
                    course.append(11)
                    course.append(-1.68)
                    
                    course.append(11.2)
                elif bool(re.match('106',str(data['e'])))==True:
                    course.append(15)
                    course.append(2.4)
                    
                    course.append(3.3)
                elif bool(re.match('107',str(data['e'])))==True:
                    course.append(-8.6)
                    course.append(3.36)
                    
                    course.append(-3.1)
                elif bool(re.match('108',str(data['e'])))==True:
                    course.append(23.3)
                    course.append(2.22)
                    
                    course.append(11.4)
                elif bool(re.match('109',str(data['e'])))==True:
                    course.append(22.8)
                    course.append(1.42)
                    
                    course.append(-9.8)
                elif bool(re.match('110',str(data['e'])))==True:
                    course.append(23.7)
                    course.append(10.93)
                    
                    course.append(9.5)
                elif bool(re.match('111',str(data['e'])))==True:
                    course.append(-5.3)
                    course.append(10.21)
                    
                    course.append(5.7)
                
                if data['p']=='':
                     s_tmp=str(data['s']).replace(',','')
                     if float(s_tmp)==0:
                         course.append('0')
                     else:
                         p1_tmp=round(float(tp_tmp)/float(s_tmp),2)
                         course.append(p1_tmp)
                else:
                     p_tmp=str(data['p']).replace(',','')
                     course.append((round(float(p_tmp)/10000,2)))
                ws.append(course)
wb.save(f'./0427_taichung/{file_name}.xlsx')
print('儲存完成!')    





#包含房地 房地+車 建物 105/2-111/3



# =============================================================================
# def urllist():
#     dict01={'437大甲區':""\ http://shorturl.at/cpvL4
#            ,'439大安區':""\
#            ,'432大肚區':""\
#            ,'4112大里區':""\
#            ,'428大雅區':""\
#            ,'400中區':""\
#            ,'411太平區':""\
#            ,'406北屯區':""\
#            ,'404北區':""\
#            ,'438外埔區':""\
#            ,'422石岡區':""\
#            ,'421后里區':""\
#            ,'407西屯區':""\
#            ,'403西區':""\
#            ,'433沙鹿區':""\
#            ,'424和平區':""\
#            ,'401東區':""\
#            ,'423東勢區':""\
#            ,'408南屯區':""\
#            ,'402南區':""\
#            ,'414烏日區':""\
#            ,'419神岡區':""\
#            ,'435梧棲區':""\
#            ,'436清水區':""\
#            ,'426新社區':""\
#            ,'427潭子區':""\
#            ,'434龍井區':""\
#            ,'420豐原區':""\
#            ,'431霧峰區':""\
#         }
# =============================================================================

# =============================================================================
# dict01={'437大甲區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/3260d10ef929853e1074f955e7aeb3fc?q=VTJGc2RHVmtYMTlZUEI0ajRsRFo4NEczMzU3aUJFMUFnZlpHdmtrbzFiN25XOGZIalgwRlQ5MGJzSEZuOUZvTEs0Q2x4RFcyb3JFWG9uVmRyMlUxS0tMZmtCcFdLTGFPWWd1aHRNSmxKNzJRL3FNMjZVTWFQNVVTSjFWc2JhWnloazB6Mzh3OFI0eXNBVDVVUGpKZDhSVnRYejV5ZHRnWXEvSFFqc21CZGNYYlNGWjJNZFB6V09zRUhpU1pQTFhhSXpyYWlRcEF0UXAxV3NkZUJHRFhHWnhFMkoxTDNoWTlNd0VRYzkxd1pHRlFzVXRzUFpON3lhNkVOZWtlWTMxaW8yZ3BXcUFCQkIxR3FPYjVvek5oRWh2RUZBb2c5anZKdnk0MlE5OXNSamorUm4xcUIrVjJnMUUxTU5EMkFDZFNISk1GM29BUFhJZEhHM09BUE1mNDM0d3lNTkhKSllkUS9WYUxnMXQ1UXBCRlpEZnZSWDVidTllMm5jZzhzRU9SdmdNR3R0RFYrTmFTMFEwc3NpNGVPU20vN0ZNbXQ3QVZJN01yTWxGK3U0dC96ZXB0RnpXOU9ES3BaRlQrbUFKeFMydXhQT1ExTFBVeVhOQjZLN2g3ZlRZRHMxWlBsczVod3V1dEdmN3ArYjNBQ09BQ3BZWlpPc1pqQS9uekNhdTJ1YVJLNG9qVkVkSUl4UC9HL1NWWlFoMis0ckhvdFpjZGNYUExIL0hGT0Q0PQ=="\
#            ,'439大安區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/53c8feb86fb3141ba10a1b04392858b1?q=VTJGc2RHVmtYMSsvOEkxKzVnQW04TTA3MWh5cnNuNlYyd1lISVl2QjBvZXF2enV6RUNnZlUxcCtJZ2dTdHhROTdNY3JMaklGVURvNFpDTlcwczhrSWVmUHFCanVSYklIRG5RM0NhcGNmZFJhQ2ZKRDAwdnVhR3hmNXRxcTFJMVpwamRYRzVWdGdESkVJVnBLRGVQYkVkeUVnK0ZROFJwalJyZ2JEVE9lYzNrNGQ5eURJTE5IaXRFUmYvSmZneEh5dEZkM0Y3dTJ5Tk9LR0lNNVBnem1OVTM2emtwVFQ2UTFEanNmSm1hNzluQTdxMG5lTkdEOW5EQnNlb0g2WEFXS0s5YnlRUGEycWpNUEc0Z05xbzcrY2ZlK0p1a2FaYXdqMUgrS1BSM3JpN3J1L2hIQ256eWN1dHV4QmNxUEppY201eVFEdHN2dndEQUNTR0FELzBhTUl4bzNJa2VseW1xTHlMR1EzS3BVdnB2ZUJ0eFRHblFyT1Nndlo1bk5uRFpUKzhSQUlHRjU1UnE1R254c05mNUJXRUl3SjNKcWQ4M3BFbjdQZS9pejMyUzFPcTNqVG1xMjBGRDFaQ3NjU3hjQXE5UUp3R1kvYlVFaDh1bXpnR05nTUFta0pCZC9xK1NHbnd2SXJtN3pBKzZ2UUs3OXh5YTFQSEwyWG1idmpvcjlwTGRpOU1hUzJyVkQ4OFNoM0JtMmJlc21UZmRNSUJXOXlVUXBvOHEzWEo0PQ=="\
#            ,'432大肚區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/5ae3f2c8c33a9b2383f4b84e8abca8c2?q=VTJGc2RHVmtYMThHZmpTUWRGTnZOR1hJZG5ONzhlL2lWWlZEdUUrV3l0M3JCTHluVm9vT09lWXlUeWxwUUFxeXFFQVoyNlJFWCt5bWVjbEhXeW8zeERYOG5aQ1Z2UmlSdWRqenVZdHprc0FHNDRnSEo4N1p1N3ZqSDRtZHp0cVVZRFpONThIbW1HdE1pV3dFdHRpRmlwbHBGUDF1TmZ3NnJsQkl5TFREZHFLb0ViUVlvZnh3OVNkYjh1ZTVsckJodVB3enVmcHgwRmZCZi9NVjFxYktVMlF1bHk3YmtiY042Y1JHV2NEalFoN2puQllSZHowU1l5dVdiVWJQT1haK2plZ0ZnS3g0YmV6REduYlY5Rk5ROWhMVlhqYnVSdHRWbzgySjVuN0tneUQxR1RaZTFpemhlMmFxNUVubFkrM2duVnB4YVNZM3RIeksxUTlHVUJXQUFFdWVaYW1lVEdSR21RR1ZPYWRCbEtmRDJnbkpQcVF6Q1dMeFVwamNFbjJLdXQxa2g4VmgzNmV6VnZQMUV0WDJJZDNSM3N6Q09rUVJpZzlyWEpTbUIyUFN0TlZuMENtK01zQlhvR3B2R3FhZXRnQnFVeUlnbmlQVXIvdGFvZENobGFTL1N0RUlhV1lKNCtkSU1GcDB1b3RRd0VienVYcG1wOTF4eFNOQUIrVWRicWMwOWFIaHlEazR6ajkxRmRwSThCZGg0Y0pqQ0NmYUVYWHhFNEJVeURRPQ=="\
#            ,'412大里區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/c3e6702f11bef642a3eb779935697792?q=VTJGc2RHVmtYMTlNU2UwSTRPWkl0REJLYTYreWJLY3N4NlJ1UklaQVk3Q2NtZ1pCSlhLSVpNNlpIN2REZTlabWJLYkNpdzRQamFsS2dWdGtCK1F2dkllSnMrTHNzUzdkMHBSbTU2RUpaQVEyR3RSR2tBc3l0MDJERGUwa3dnS0Q4eXFJbCtqbTdPc0szREpMMmg2S1VNVnBxZlJQQkZNT3oyU3R5UVAvSVhjaDNpYVZBV3IzVklrSHVtcUxPMlpqK3B3OXdhcVMrL0l6RUJIUDI4YzVMUXpTT05aQXhFTUdzbm1iS0J1ZVJvN2RzeTlRZzN2QjVjWHJUTUoxMlVValZXanM5QTBJaDBUMUdYNm1hUlpDUDVySXY2Q2hxdUVHaWp3T2JaZC84NDZnRHV0ZCtHUlZoV0ZtQ3NzanphNlNpRG8vaWQ4NXNsQ21pYVFjeUVSZnNiUEhnSUp6MTFUWVpvV0Q4NldtQnFtVFFUUTR6c1QvcUtHMlBldUVpNmdyRHcrOHN5S3dGMEdud01uNzVWUFBPNWFQTENyTklaSWRsOGdKOXZTUGNObWFad3k2WjN6SU9Dc1g0ZGViMnVuR0Qramc1TUFPS2Z3anhOVmZuSm1NRlA1SDNWR0VVV0kxalU1bmN2bjR3bnRQTWJZRWk4cC84MXhWckxaNUpLNVREcFRaTmt5Z0VxUkdHNVhzekdITHd4cTJOcWI4UmIzRUQzQjg2Y2Z1WVdzPQ=="\
#            ,'428大雅區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/aa376e62d715e1d5483f1023419fd155?q=VTJGc2RHVmtYMSszTmdEWGpPcG43eDQvTnVOV3UweThNOU1LQThod29kbjdOZUIxUURXWFlVMzBjckVSQnordWpMdUlQTzYxNWRVdWRzMzRmalVORmFEWk1VY1lQZWtCd3oydHFDcnBPdTRXaThxck8zd0N6Y3IrY3FLNGdjK2M2MmJaRzV4UUR2M2xYek44VzNsVGhzQTl0UEx4Q2dJQitPd0h4QWlJVnQ4eTF1MGJlK01pMURhY3BtTmhZYUp2dXluTWRQdXg2ajRyUVQxbnN4NjJzUHpzUjNlZm9vQUJXb0I3MmZGcGdzRmxML2ZQcnR5Z1pwT25LTkxLTTdBd284VnRpeHVBbjEzcUJSbjFsekw3ei9VdjVwWWttWm9WTE92Y3orWWFOaEsxZmFUMVNFdStRQjZ1V09RUnlTdnNzZmJyVjdBK3JCMjk0ejdWVXFxWDJUZ0t1QjBMcmR3a0E3STZoNUVqY2ovT2dTRXNPYXJWTGZSNUo0eUF1SklTRXJSbEgxU3ljQW1vVjlZb3RxeUxuVEV4bHowMEwvWTQ0ZXp0Q1dMeExiTlcrWUFKTjJRcHlrN3lBNFV2cE53YkdtWlgwdENJZ01EQkQ5L3k2QVdtYk03Vm9sYkJ0UjhYRFAzQ3Q2eThpVHlQNXo2NmpGbEwrRzV3emlQVU1PcVp6QWZHUFlMYmJtYzRoZHAyTEhrY21KRXlYakNhM1NvSU1DN2txSDMxTWlBPQ=="\
#            ,'400中區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/9c0759cb9da78af0ed7d830632e7a7c5?q=VTJGc2RHVmtYMTgwU1FZa1ZCZUQ5ekpJNkltSGw2bDRpMUNHemhkNXE5dXREbDlUaXo2V3hZZG1icUtRS0dMK0JEMDRrT1FtTUxQcVh4em1JZTNpUlBjTFZCM0FrY1VJQ2ZIS0dCSzZRd2EwNG1qb2ZsQStyZE4weWVYL2xkUDR1cGZJYjMyZU1HR296QXorby92d1lGUEsza25LbHBySXV3N0h5cFE5YmF5RG9JVHVHTGc4OEIxbTZZMGJKcmN4akpZb2hGWGJhV1EwRGhQeUpQTU41VFY0VkxCRXI1SWQ3STZlSWowL0Ywb1VRbTMxd2hHVHYvYklDV05hYitIYThIRWs1UEhML0x5WXFPcnAyWEVjeXZUUjdXcGN3QjVycnJ5UzJVUFZKOWRpQmMrMWdTTHdYTStHRmFERHA0QUwyVFY3M05Md2xzT3gzUmQwVzN4a1F3THRJV1VtUUJQeWNGTXpQeUQzY2lzcC9HTmpGREVSY2NIL0g3azdqMHRzRGNadEd0OG1OWWMrOHVxNzEybnVSVTRCckdkQzdkUDh0TVp4RkNmeTZOS1F3MEdNbzB4UlZ3YjF3MW4xbzFraVdkb1lsTE1mY3N4MjNZSjc3dmxtRy9WK1plMERPOXMvWDk4Yy9CYlpPM1ZOcHd0a2RtbWhqeUQzcFFCYWJvZ1BMNUNFM2xwU0lJaHlMK2hvanBzSVZPcjZnRmYxRXQ3OGtqSFJPakpkZWtFPQ=="\
#            ,'411太平區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/357055d57aee72ab014dcef0fa9c6fe1?q=VTJGc2RHVmtYMTl1RytxTW5nUk0zdGROQnhxcTd3NmFLSzBIdDY5akk2aklRL2Nac3VUYmtKdEFHVFQ2TkswRXdrRlo3MXVYWkVrN1o1TTJhRXFyemFyQ3ZYbXBydVY3SmttZlNOcHdRNmk2L1Z3eXIwSzJiOWxqM29UaXlJQURuVUNTTXpFVDRRVjR5Q2ZKTUhLWmdzUWdPOW5pbWZsbFRIN3pTaVJZcmJHbjlPL0NwL095SGRtVXloWmoxOFZDTm40bHBUMExkWEVqaE1nRG01R01vRHRRZHBCcGRFKzhBK055NEJpc3ljcjMwa3VYZnF5eFlKSVJHTlFzSWtwaEx1L3grZEVnT1dzVG45VjA3Mi8vR1kzT3JvRWtSM2tJOUVLcHpXSWdmdThjeks1VGtidDZtT2dzMVJYT3hNRURUV2djZHNXcU13ZFVnaDFaVEdwY0JQNmV0V1kxbmlESTNmRHNGNjBVNUlQQ3BBdnNKaHFzeHlFT0V5WnV2c2wvK0VjeGFDNi9vcXdkRGp0L0t0QnZqYUZLTFQraEw0OEVWY2RRM2JsUDBNNUxQbkJKUCtYaDJJNHBQSjl4RlJpM0t0NW1WczBNVmtqMXpPazk4NUxLZlNvOUE5dldOQ3Vvd0ZZM0Ftc2Q4bzd0aVd4NWhSaWpIakc0Um93ZlNGRU5pSlkzbG16c3VFNHhKSmx2RnFWb0ZpUGVmS0hoTUVpZVp3VFpnU1NwMUFnPQ=="\
#            ,'406北屯區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/f01d5d64fe93cedd38eed851a31519bc?q=VTJGc2RHVmtYMTl5RUo0NFQvTkJVeUNONHY0RkdTbWxBNlZpUHFITXdjdFduN3A5dDlBVzU2VDZFK3FZSnl6dHZIVXVnOEtqaXFqNXE1WUk2VG9ZczhmNklrZFNvVk14TzhFSElnWVdJR0hXcVkwWmxhMUVEYWZXOG5TTHZUWTVLWTZsVWs0OHN2Y2czb2RLd2xadWRxVWcvTk9ZQ2J2N3lMa2xzampvd1VPdWh0eEw0VTBsUjNZcDRjMmF2VWVzU3dmRUhjdnI3WDlsSVNyd0tUSmMwM1pvS1RuUHpNNVE0R0FRRTI2YTdzcnJoeHJxcVRobFJYV05FTUZDYmVTVitLUUcrUEZPWDlOSlRybGpnM2xmODRCVEF1YnFFME9lemhNL3FGR2NMSXJGemFXNk1QZWJ0VnlPSGNGbFg3QWZhbzZpS3FGR3ZQZUZUTXBndFZRM3JiZ0JldUR3UkRXcGsxcUVmTWFDZVJya2hCcHk5b2IwVVZaM1JEQ1NGa0tkWnFYN2NRWm9uTVhyYStyb2Qza3RLWHgreXNjUzFmUWYxVVBoSEd1OCt3OGdYRlpwR1grV2VsK1R2eEIvREdzb01zdllFTzVENHR3a081RWpkYmNuazQvQXFycnZ6UDZlczlwQ05yeStVc05tK1JKMS9FZmZHdFlvWWlXZVRoN3hSakdEQ1NnaS9najJjaEMwanJhNG81L1RYcjg3d2lGTzFTd1JFOEZrMlhvPQ=="\
#            ,'404北區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/54308d2c92ac5ba7a5792ea06ab164d0?q=VTJGc2RHVmtYMS80dkMvWUozaHBjKzdSTGR1bVluc2pKeFZYMXMxNXl3dmh0U2tPSXM3Y202a2k4VzA3N3pLaUN0anJJQmdWWmZxYjQ4eTBCd0wyQ3JKQmI5YXBJdi9vVTlXVnR6QUZQMGU3cHBoVm9SY2ZqVFdKb2Z6dlZ2SG02Wko4blA1Si9tMmowczJSKzZmQld3dGY0cGVuWU1rbk1iTmQxME1ONUpYMDBOQWMwR2JzcC9VR3JWQ25SbEdqL3g2aDZNLzk1VmVXTlJCUEV5NUtHazhRVEhXNXhiU1A0V2JTTHlpYmplVVc1WlVPVE0yM08zaEZvQWphL3BzSnVrR1daY2RPZlJERytVc0VKc0lhQUljRjNHSnh3ZzNZSEZzaGJ0MTZKeVVqZHdwSlp0T2xNRkJEekFJVDYxYS8xMC9oM0JTeDcrWTRaUXRhbDRWZGtObFNxQUYrV3N2SGM1UnMwQm9ZMlB4MlpiNEJQTmZnd1BNalhyN004c2FnNFF6ZXNScXRmNEJTbTlyS0NuMTR5eTdpbW1BeUlOWFQrWnA3UHgzS2V1eUFwZC82QStZRmpjTGFoNEFlekpPTkRPNkluK2orZ2FrWFZkbURxTzl5ZzBVS3JBak8raU9nSHdKUHdvcG1SMFdrbXhWc1YydHNnMGY0SVZGMmJ6c3JWZUJ3amNTUlFuTTZCcjEzamJWNEw4QStaZ0RCa2FOczZhSkdRTitMYWpvPQ=="\
#            ,'438外埔區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/3a47a42e96ac338dc9bb78ce5fc074a1?q=VTJGc2RHVmtYMTlrWVUwQmczd1dKaUtMZFNMVXA3NVEzQzZsSHlDL0xmcis5NkpQQjYvYjJmei9uOHdKS294WkROS1dGL3lRL1FWbjZPYUtwM3NZbUY3ckdZQUErZDg0MGU5azVnT1N2WUdibVVPNkZ3UXVhUEFSWmYxY3BOYjRwU3RuVVpMNDhwaHRhc3JlbXE5emFiM3pwbUZjYjFjNjJXb2huUnFRWktUcjZ5UE1uVkFUNlFGQkVCTFNpQUVNNURQTDdrYmlYb25DMGkvUlpGOW0wYmF4bnZTVjlQK1NENzV2RmJlRWRPS3JCeW9YYnhCdGlVcllsL0JMbWkzMTJrVkFGRkJxWFJCc0JZMmhORHN4VE9wUE9pWS9xRmNxc1VxaFVsNTZWdE9reDJMOWFyTlgxQ0hYYy94Z2tmU2JSMjdRZUZFNkZ5YVIxY040RjJrblVManlTQUpuV2xtTTZNUjQyVk5DQ1JSS2kyZnBacXpWVWlJTnU2SlNIU1RIS2tUU3NsRDhPRXhvbG9JdUlpSVlRajhibzZzRGpyQml6RFVTbkUzY1YyZTM5WlZTTGZ3OFEvV3liMCtSVEpndGpSZ1VCdXc5MEhpdVZaWDVCMVRyQWxZdUJNanZPNisvOTJWbmQ2eHVuSlBZeXNKeEpwZGhzUE9CemNRbzVjeGxSRFduUHd5bnYwRklYVy9Nc1ZsdkVXdDZBWUhpd3dZK1NxMi9JR05UOWVFPQ=="\
#            ,'422石岡區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/61444364e3ad6507481719e495e145e1?q=VTJGc2RHVmtYMTlGeTdKbUdnemUvdHU5ZUVxdmZnaWJFaU1HVkZnYy9KRTFxYVhLK3Bid2NoRzJJaGJibEpQYXJPSHZKaUh5UWhDbldHUDVxV04zQXE3Zy9mQUM3SzNZUktZNXd2dFYwY2lObURhcWY5V05paEFqRWk5M0dINUVLbm1IbWphMlpYNFdqMzhydmdrVGkwSGh3SndJdm1DQWZCa05HZXZaZ0VEbjNaREgwTU9QWmk5aFpxNW5zZnpZbVpuZkQvcENHRGFJMTQrb0M1aU91a0o5RGJKTFlmV1VHL3B5bnIwSFhrb1ZCWkZON0V0YkRWK1RsN0JTQ05yU3FXL2dNWEhQQkJPR05SejU5MDFuZnJXSm9nYzlhdDBiaWlFejR0cmk0V0VDeEgzZjJ1dUFRVVdhWWxJZ3ZYL01jaE1GdVNuRlRzZ0JhM2RINCtyMW1xVXAva1lLZGJPSFVUSk9pL29mRDNuNm9nNktGUjlPTEV3Q2lCM0tKaVNSS2J6UUM4amtnSlNzdTdSNE1PaUczaEhkaXV3UVU3MHNIUXpWekpselJxb2Jsb0c1ckFER2tXMmRYZlZhZ0VOS2t0eExKclMzaDl2VFlYeXhmbW9vRFFxcjJGOE5yUWVLOWlLdnRLcDdBREVFN1NaQ3pyNENia3JkalloejlLam5GdzUxSlJZc2lLQXRrMFdPQjFwUmRZVjRtQ25iZVlhL0dWaVhtUVNXRU5zPQ=="\
#            ,'421后里區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/3e93cbcc4eb4022790c0a3424e2829d9?q=VTJGc2RHVmtYMStNYjZvNEM3aHYwMG85ZGNDbjh4Slp0Z0lqakRQd09zR3huTFEyajBFZ2JKV1RuRjhHV3g1aG9xeGsreEFUTkYzNjhPMmwzdFVWS25rVUpxNFh6anNVd3FGUVZQdjQ4Nm5CTXdTUE1yZ0tLZ2tmNXd4RHN6dFhMR21GeVVoWm9pZm5tUnhqK1NlOEhvZllTQUdDd3huQ25Eb05HQUc5OTVPTVl0aEtmakxmTWZEN2tGQ0Z6a1I2VnoydGJDMDhXZTV0cU9mMTV1QzRBUEY0QkxkcFdaN0Yvb0pqVldvYWxhZS9IRUVQeEYxL25Qb1NZM29aQk5jYldPSWpWZzBNWGZvRHIvTno4VnN2VGsrcEdmMGkxekE5dDdUN1NzMG1nUGROUmNGVzY4aDBiYXlyWE1WMjVuVkpZS2drY2RmRlF2S2dwQ2p4UXZUWWovK29rQnhMNlJORGoyYmk3ejN1TW5MSDdsTVJxY2tsbTlodFFQdXo1UTBDaStsVXBOdkhpemRwZWdUUkt0OG8yR2MvRGUzSmxiRzk1S2l3Qnl4c2ZaZlNtYzJrSkxtQkcwTDZkcDlVd3k0SUJPYmQ2THJ4ZER0eG5KZTg1UDBBS2FKbm1aWHl0Qm52ek9idUo1NWt1M25mRGV1dU8zTjJyQVVtKzU0NDNyVWRtd1M2dnVoN1V2bjkwa2ZTYTcwL2o5T0Z4SDlZbXlCYmo3Z01QSXZnYVNJPQ=="\
#            ,'407西屯區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/d58e6346ba9624cfb743cdf97d5da5d4?q=VTJGc2RHVmtYMThwWm5SaUs0RzN3Z3cyT1p0a05tWVZISFNXaDE5OEdaWHpGOEpTNnRic2JjcEVQekhNaDZOREszczdKR0dRTlZKaHBLbDRmUWxCVWNxQXk0K01rSzh5RTJlRFB6a2srby9OUWdza1BxbWZkOW41eW10YlZxRURZcDdkc3JkUUpNY1J5TVpWLzN4bDdpQVVRZlMvMXM3RUptcjlDWm9RMHRlRmRiMW04SWx2T05udDBTdWV2L04yL2ROcFZTMFBnT3J2eVlkdVBOaVhZUmhMVHFoMG1VSzFJRGNEOEszdFY5dGs4Y2E3TkZpcnlIYUFaMjZLWG9tcktYaXRiL2RadEFybmhhcy9xU3QwdkJKbEJCaGIzY3MrVHVuK1Z6ZWo1NzJic2ttVXcyZ2ppNDIyWExtRDFHM005VEMrNm5pUXVSa2UrdHNZTWQ3WTNGTDRtNzJ0R09ZcXo0OTlmQ0V0WVdTTGpZSGpFSnlSdTQ2N0ExZGh1VjlBd0pkb1dGMWhGaUhkSjdYWmlyOE5JN1I0dC92NWZ0OHA3RG5tMnFUR0FhSnY4anZJaUdTZ0NIYVd5Vk12SVhvMXRqOHVDOWRPc3p1Zm1tc0VzdTlrY0sydFI5cGxNZjBJTXBSWDZjU21DbXJTZ3Q0dTdLTTh6clRESElhRVdndVFFYUgwMUJuRWQxazFrYlh6RUdWVitlcEhBQ0IrZFFnSzU2d3lHOHdTQlhzPQ=="\
#            ,'403西區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/d9864af4ca7504c9f2cfbf617b24762d?q=VTJGc2RHVmtYMTljdVdnL0xERitUTDhFN0lIOEVSUDE0UDNjRGlSSS9uN3FpSDJvenRJUERZZExMRVM5OXZoa1o2NnVFNU1xT3F2SitSZjVhTGpoaUNHTTY1Z1IwTTBFVkttVWFRTXJqa1V0T292cXBIMlpCbVBUNk9DN2czTmE4Rzl6dW02RWdybnc1ZkM1OHZjbW4vbUhJOEtpYUw3VVpCYTNkdUNSUE44bEdMd3RrajQyOXBoUlQxOVpTMFptNnVqc1hKN00xRmVVZUtQNE5pc1Q4TFJYT291ZGNJTFhuc1FDNTkyb2Q5Wm1xNWh1M0V5VitkRVJwaU03Tm1qKzROREVTaTc1WFJrNXlNc1JRd2xhZW1JWDk3QzRFOFRDNjNnM3FyMHVLWTAxTXNIMnUrYU5ZZ3pVRThSR2hzS3FlUkRxQVFvL1pQd2c0d0ppMHltTTVIQ0NxTHZzTHBWRS9YSlhjY1AweHdoWFFvMjViQUJjOWZEczZEMklSS3hDQXBoRHRxVFV6Q3RSc05wZktRMGZ5SjJvcEF6bXJ0b2NDNlBBWXdqVVpublRnZWJ6TU5LaGZjSFJxdzF3Wm83VjhwdmZLOUFHQ3d0bit2bkl2OCtSajZmUlhqaWlyN3BuS2VIZmdlWkx0aVEzdmIxQjBtdFo3SHIwNXAzejJYMndoSi9GRkh0aU5lZlVJbEFCWFZpVUJ5SGhoVjhMdTNPK0lyYzk4a0J6WEFnPQ=="\
#            ,'433沙鹿區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/1a09502373c9943ec5e43d7503597f92?q=VTJGc2RHVmtYMS9YR1FKd1EzUjRXYmZyOUduencxeENsL0gybzYreGl0VUZLR2VhRXhwSkVHM0J3bGJNK0hRanZFWDJPang3eHI4aHNNb2FZQlZMU3FjaTRVczdXcUNBcGk1ZngralpDR1VIcEsxK1ZPNUZMejRuS1lGZ0lTSXN5NW9yVlRISVFJWURNSDFBcGRNM2pRN0pYYWpHQndhVHRmajErOE5aVzR2aXJtZWlwM2F4bEhueTc1K3Q2VFNLdmN0dUNHK1VLSkVWbkVPOFNKTTVXYm5wQUNYRU1YQUtRdjJpTlhSUTVRdktzVHEwMURlQWVtQ0lLV3Z4SVJ2TTc0eGVLZDdCcE5OcE0rVndObUV2MmxtMDBiWlJaWGpVUkhIc05kc2xBa3B0YzJmdFBVMjUxWllQOHJieVlRSkF5a0xPMXg1bjMxN0dDNVVaeFE5MDhzZFZFZFJFQ2tkMlhWekg0LzhYVzhGUG45YUdEWFBhMUhuMmUvaVMxcEtZNWd1Ni9LNmQzTHZvZDhhVE1rU1NROHE4THd4QVFxTytpTVpkS2JmWUVEbHZuRy9jWnR5SXNlMDJHY2d6MGZQb0F5bVRtNWl6RUtUTVRwZjNoQ2pSR1hROVRvbFkyQm5kQ1djQ1cramFNSkZvWmRHS2ZodTFKYklHdUpKZUJDNzlIUGlDWFRmUU54ZHVFSHFrT1FOeFhDeHliazE3eEJacGZya2Y0NFdxRy8wPQ=="\
#            ,'424和平區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/8bb1e688746e5834fcc66fa83d954251?q=VTJGc2RHVmtYMThYMzJJWFpFVWtmYStpL0JXOUtpSjB6QWw3MUhZcmhzVnFWU3hjQndlTk54MHU3UVZNdFZWN0ZMS0xCcDkyNDRQVDYzQ2J2TDNUanpHdko0M3RtZEkwdnZmaHo5MGRYL0xaWEQ0WW1yYTR0NElibktzQ1JNNTRoN1RPYThnQnBIL0RaK2RtOUFxRjFXQTJVcXpDVW5KY05FUW83TWduSU9FWlN4c3JxZzJ2NDVaYXBzRW1tMG1ibE5ySi9nU0VYc2RySFk5OFIwMDlGN2RwdCtnUkpWcDg5cUhUdGE5a2txRnlTYStwUWRTT2RBWUlhNEZOc2p2L1QzaFlDL3ZCcmhJbWhaOWFtdjFXRE5uWHAzRzF4YWN3VXU0WHlDRkV3bnlLUWdiWnh5Q2tSSDJqdjEranBtYlZjRk9XZFNlYUFkR21QcmpzT3dzRTBId25iWmdUN2NZYkpxM1lBRlZKNm9xVUZCT09qc0FMWlFsc3FOY0tHRTAyM01wenQrRjBLRzZVeU54U0lqMG9ReHhYcE84YVNpUkFUUmxQUGNsRjh3ZVU2dmYrYzVrUGxkTXY3OXA2M05CRFpJSnJ5RXlyTGt1bENMSzJCeVY5dG85Q2RlQ0NVNUdKMXhaWXpnT3c2V1BnUkpGZnN3YlBIZUM5WTZsYUpydHpra3FwY0dlZklLb25CcHppY3JBYWZDOU5MZzljSTRnNUpFTG9CSTFwdkt3PQ=="\
#            ,'401東區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/576e6fe1720c94918019cf7b712ab8c4?q=VTJGc2RHVmtYMTlhNUtudHFJTEpDR2RxZHdLWHE5WTA1SVpFNU9URm1tMkcyY1l4UVl3bHBnbmpXMjdiMThRS1J1bXJIZ2RxVHhvbjNZQXl3aUxFa3E4Nk11Wm1xcU1IamhHa2VaUWNVcGtEQjQwZkxaSGNkaEpiRWxLNTk3SGJ3U2xiY2hmRG1oaDJmT1FlM21Hd0xFZGo3U3duN0dtTUNIQVVxWEZuZy80Q21GVDZDRlhUVFJtelNkZUpTdHJ0Tm9hMDN1M0d4L2JtM2N4TDhaeEwyUVhKZm9kV0ZNOTV6RWptZHZucTYzejJ5T1JQZVFFa2ZkVm9YTzl5YnkzSW8vMzB0dmg3SUkxLzMxRkFPSXBQQTVBdnIxM0tQNDhvcElnbkgzdGpQR2J0dXF4QnExREVFaDNoSTJwTEs4ekJsenVjUFNtblhTek1lOC95akhka09mUUJIckUyN3hXZjZFd0pQR3R2TVErWXN6RXJtQm9DVU04THFlQ2FaQjRkMHFBcUk3TFh6cUd4QldrbmlUNWRVZW5JbWxjQTEva2hVaU9CcEEwa3M5eWtTbmg1ckswbW1HaVpKSEQvbkJNSUJGclF0cEdxYTJrVXRLNjJlYUkzMFRWQ0cvbVE2aEpmdjNFWWN1eWZ6WmV0MEpnUkZUbTgwQUhEanN4d3FYcktGVWRQZU5QbzhYMk4zOUREMjc2RHJzYnRQcDZ6K1phcjZHc1RrVHpHMU8wPQ=="\
#            ,'423東勢區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/57babb8b7155879c79da32615aff931c?q=VTJGc2RHVmtYMTlrK2pQZEt6M21tcTlkSUVucHBFUnpqWStQUkhHSkovNURXMVVhd05MSVRtL3AyTEZIYzNKUHkvUUF0KzF1RzNaaGJPZHJhRzVYa2lPOThlanFEdEFCaDZCa3dIYnhHVm5Dc3hZdU4wNnBpNWFsMVVuR2YvUVUwdVI2V2lZRU5lR0wzZk53RWUxb0hXeE96a1N5VHU0YWpkb0x3MnJjeUFsY0VlUW5XeUo3aE5YUDJmZU4xZHR6Uk9ocDBnUDZlellHeHRlSSsyczdobkt2Vk84azUyaGtoREhqUWxGU1lLSTZpQ1RMbGJ5bS9CbUNYZzNTYm54clVRaXh0azhZdHY1clJFSlF3bzk5aU50bWtJMmpGbnNTYjJRQmRrYnRKczRBYXJJRE12bmxMYWFPaG1nS3E1bXIyN2dwR3U0emVaNEhUYjB3cVRaWTZJcXZBNHJpVDN5dXNuVjB0MW1XNEFBVmpFVjE3UWNrQW5VemR6WkZtNWt4NlU2ZlNXMFdmaXFXOTRWeEticFVJTzU5M0NYamJmOWVsWTdJMmt0VXdvc053YXJJWnQ1QVI2cTVnSERoNDVMeG04UFZKdUJXbGVLL1pTc0NqdFI5ZUF6QXlrRGxEZU13R3crVGRJNk12MkljNjBIUm1mMlJoTnlsRWpFbWY1L0VLd21VZ2xvUlFwRTcwU0l4RVJ2MHd1allLdVBPZXE2Z3B2NEl6K3l3MG0wPQ=="\
#            ,'408南屯區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/fe3b32869e8a04ed3d3fb99aa97e0fd8?q=VTJGc2RHVmtYMTljTU9kNHpoR3dNTXNjM0szbHpyKzNuSFhZd2hKOHJwMFFUMjNFalBlK1ZmRmcwdWdoNmhFQVMrMUdQcVFVQWhuWmVLblozay9JY0Zkb0xIbGZyY3A1NUt3UVVmZkRpcVJEWGpTNmliZEZhV21HaURZVXVXWjVIZWtrVnJCaHdvMzhEditNTmFHUzNBSGorK1RjRGtQTFh6d2xtQTZUL1hkV2lJdy9oVXptVEk2NkJGLzYrdDQ5aXg2TjhPa1JpcUVOVmladXdiYWpQSEU4T0NqUmxBdXRHZkV5SXdBWGdpMUJnRVVlMEt0TWVvVEVkR09FZXArbE9uYUZlcGJYQXNuZ28rck5VVUR1SkYvRHVDWDBZc1ozMHRvM2xhRktpTUVsWXh0VVNYWmN1OU53YW8rY0JNdUM1UDBFaDZ5OXdmSHlRUnZvbW5XWmRsekFKZW9jQ295eHpiKzhaNGxtYTh2MldIK1NrdjEyL0VxdHV0MXFhZVNhSDQ0clVaSG5Ld3JGTEIzT2xmUEZyMUhOMVl2TzBETENEVHF3bkxSNi9mNlMzTHBacmM4U1VFUWYvYjFaUVlTbVBwNWN6alJRcGJPRE4yZ2dKOGZOMDViRnZCSkRFNWsxdGcxditmeHFmbDNtSVdLbUgrWCtFcXdENW1XdmNSUVE2dmh1NEk3Y1FUd1kxNzdqYkNzU3VZWHJLc3I0UVVxeHBjZDY3WW9vcklJPQ=="\
#            ,'402南區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/df40794cee9db021f669fab9b740d3ba?q=VTJGc2RHVmtYMS8zeWtmb0s0bk16am5XcEpMMERzdEVLeng5RWV1bml2U3FrcFJidUVnRFRxWXhUTTJ6SC9URXBpMmR4cnV3Nkh3M0IzRXBRdTVOSlkzZzErblMwdjBZa0tkaXUrTnk4enhYS1B0N1dHY1pneVIwRFUvZlZqbDVOYXM1QlZKNUZBb1AzVjU4V0VncE9yVDE2ck4zL2R0RlE4Q1lDMkZvUGdvbXV2MWkyeGd6bDlYdzQzL29UN25jNVFTL2QwL25va284Y3luaEE1VmNPYWpiTUFQSHNqYzF0WE1ENHZFRHYwTWJ0djlWZDcrbVFKTkNLRGFqckRBV0ZPcWIyZUkrM21TWmhlU3lyYjF4R0Fsd1pxYmlBUnRXOFZmZVVDQTFUaEQzT2gwTnFFUnNablhSekpqeWpYZXluWkFtOFFzR2FOenFKRnB5b1dpd2ZhTEt1NnQ2dkp4cDBCWlJtTy9yMUZ6ODQrUzMra1QzUWRrMjkveTloZ1JpZk9vejZIVHNabEhNT0g0aFg3aFplNk84elc2aTRUb1N2dmlWK0U5KzhManpmekEwRnpzYXNseUlwUklaaHdnM3daTmphaWRUN1JaeURWcURkYUtwdGp3V01ucUVXZTBobDcxTnlUNWZ4ckQ0eldGR0g0NlJkclFkVzZ6aVNrQ1lsR0xqWTRNNVRLQkU5SFBMN1JjZitSSnd3NERMUUIvTElzTzkrTFhVdzlnPQ=="\
#            ,'414烏日區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/2cca336ff65f6579a9a01b0a06c420b4?q=VTJGc2RHVmtYMStNZTRlWEdJTVVoVkNMeXMwUUU2UG9vR293cWxaVjhESU1YMmZlUG9ya1U1VU10TjZzQWhma1hMRzlEa0I0R1ZLZDc5RkxLZDVqUzVZQnQvdUV4aXNpRndYSE5NZjJEUjdhTFRUK0oyUlppc2IyaVRxamdRY1ZDZmZmNk4xRytacUpqRjJnUFl2QnRhZ3lRZXpuSy9vZm1DdTM5ZytHWTVzaHNqd3A1c21OcUN2Q2RKejFkaDFzOW41TmJZbHhlcDcyK2tsWHNrUnh4cFJWakE3QnFqbmxST29HQ3JZOW0xRVhoa2xhUTFiMUplaWNqVkE4eDVRZi9sZjdkNzRZWmNQSGk1WHV2NkN6ZTd1eHN1YUp1UVhpdFphL2U4YTV5aFYyV3lTejVCSzF2WUFteDdyRnovV2k2MFdleUpOd051YlN3UDR4Q0FRTDhKWUgwVDFmU25zNzczUEp3TThXSXRWWFRNeURxWXc0TE5SVHovZFM4QWx4Z1E5cmxNc2I3ZXNiUDUwMzR1YWJGTmllbDI4bXVSTk1VWEh1WkhVU2c2em00eCtneTBMMkZNSHp6eFhxVHMrTWFCd2RCK042SmdhREt4K2FxS2hHZ2pjYUpOUlUzSTdLbUF5S0lJNTZQWGxxRE1mdmd4TWxnRzdacmpoSFY2ZUNkRkUzakY3Y0l4bEFtN1Y1c3ZCWmUxTnBxbmZOY3l4QTRsSXNic1RaaXg4PQ=="\
#            ,'429神岡區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/7aa3e55cea5340cabfd147a6bec2bbeb?q=VTJGc2RHVmtYMS9ySjd3UEVTbnhtSXo0cVU1NkNJVXhQWVlkUlhWdXdlaUhIY29zMWx0YUtYeWJCOGtaazN0MGI4b3Z5cWFRU2JkVGxPL3ROdVVGTGpLTTlYN2V0WWtkWDlUUzhMTUhGMkNpUlp1NmEvUEJobjZiWStlSnF0Q3d3MXBLYjFaUHdBa0ZoNGRMMjFWQWV3QS9LS3Z1VnBDMU9va3FnYnpOeGpsRXlIVTU4VFJQdDhIWjQzay9qNzNPaEJmdnZqUmZ2ZW15SXkwRVJUVW1pbGdTZVk2VU9FbEhheFA1dzhTdVpwM3VpSWRFcll1M1g0NDJGdHdxZTJkMFhiMjl4Z29iVkFKZFptNG9YQUx3R0FJeEJ5aHdjMVFrMmNidDQrSGNQNEFKV1BVMGg3QlgzVlo4ZDNmdlZnNWdXMmlHZWZVdXQ0eFRKYkdDblBUeUxPM09rZDBpbjkzSGFLUVZ1NFpWTHJXTktpY2d1N2dEV0o1eC94V2d2RlpaMHRzU3o5YkNSSlVGNnUyN0FOWnp3UVBxb21IR1JUdVVxbGVsRXU1OE5hUU8vRkgwVk5wOFhPRXpmYjFScEcxaVlBYlNXN25uR2hJQVVmRUhMczA4OGg3TVViblhWOXI5Uk51d3lXMW1FdTRXeXZjV01tSUdlQTdSSjl6MWlNRWFNNlJNMGxtUDNxUmorYklhb3ZRWDAySzZTRUxHMEV6TTdETmNrUDBpTEk4PQ=="\
#            ,'435梧棲區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/da15b151ffe16078aa0b02ccc7d1c1b7?q=VTJGc2RHVmtYMTkzd0RCMWYwNGV6L2dDR2lobE1pRnMyT2NlQXZpZHFsYTJKVkhEek1wUDdNWjBlQ2Z5MzQrT3NtY0xqSUpqakJpSVFwZTlMNzZMM2FybDArbXFrUitBOHhaWFJjaXNJVGxYdUxoT3l0Zk1BclRFejQzYkNqSGthdjJmSWxuNE0wYldlSno3QnRySUlNV0RiR3lHNlpJdzdZTDhhMGNXVUs3TG1yK0V2LzFLdUNaek1YQkVseGlFZHBjL2RYU1IydjRsdy9IL05VV0FZcFQ1dWUvNmE5akhzWWtXdXlRb0E3TFcrY3hVK0Nmc05uRDM1dFNhaTJ2RjV0K21nSXZ6R1ZwNmhhdFpkeUovTENVNWZpdWhWbkl3Zk03OXlpcDJsZjFkMzVqK2p4V2g1TkYyOEQ5TkpORWpVNldQbEhnYjhrQzZ1SmNLaWxSc3VhNlBDN1BkWTEwc1RmbnJVWHY1cHhRdjVvTnNPT3B1UlFRNHdSZWZTT2UyR1F4U3RmdWxOVS9vUGp6VXdSeG9HV2o4RzFJQ0tFRnVXYVBzT1dQR3RvbzAxczAvOHdqTTdROEZFdG5GeFNuMGd2eTlPelZ1NXZuNjJhWlZlRjNicTRQS1BPZi9JTjhRcUtsT0NQZ0F0MXpld0laSTFwYnpNMEM1QWE1Umc2Q2JvcU0ydTF6a0xCUHUzQzlJa1ZiU01GOURFY3VsMmwrZHpEREl6akYwV0MwPQ=="\
#            ,'436清水區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/7ce123f6115f62aea49cdece4672c86f?q=VTJGc2RHVmtYMTlpL3l6ZnlhcVZHOENQSGhhWGV1ckR4TnFMZVF4Sm5QbGExOWZ2dEt2aGYwWEQ5dEN6SnQ3N2VFSjZhK1Q3eFZRSVNCcVVBQVdHbUh5Mnh2VXZlWXpHVFZwUFo2V0Jrdjd0ODhxSmlFd0VBTkpEUml6Um5wWlFKNDdrU3FieUh5ZzhiZ0NzRXhWYVVGcng4WU4wdlhqRU9MTmhYaUsvM3o5UnNkM3lveTVIWUJ3ZUEwbWlJNWdHaDJaUmtyZWlQSWFSa0lCTFdEMWY2eExmcXk5bGtHREt0OWxWQWl1OGxsOGY0eU0xTENoUjFEblBzbjFJeHo4b2I3Y29rdzcwTjVYTkFLUXZQU2h5NGFVMFkyNTRaM2hhZlp1RGZaRlFoZU9kNlFFVXkvb1h3V0MrdDBQQWJLTmFETkN1dFlsZjJ5SVloY0w5YTArNmFTRjhCTk5PR0hKcDBsK05GcDdUMDNiVEtjMERDNGNkWjc2T1kzVDJ1OVRsU3BJdHZFRkg0Z0FzZnlQZHNYQTV4QkFqUmNZYU9pU3A1RThud2YzYWhtOFBaNGlvekNuSnJ6WFlEKzJaVHZCMzROejMwdUdwME50eWZZK3lZQW1EaWZWMmNsRWwxeVUzMXBFUUJiOVJLQTY1d2dyRmpLQWVTMklPTkFuT3IrcEU0ZjB3UlBXNVB4NkdaZCtzOXgxcFlMbVIrQVZoazMwYThWcU9ZY0VYbUx3PQ=="\
#            ,'426新社區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/241b88932b22c4c4bb283f731cb6f0bb?q=VTJGc2RHVmtYMSt4ZzFya3UxTUdja1d3OXlmSndOWXRDZU9vdnowWkt2ZW1oV0tBRnFjbjgvbFpiTStabS81QXd5OTlaRnAxN1pJU1BVeTVQVE5aSldScFhLZ3JTSkE2WkY2b09JcjZ5M0h6RzRQUHQwOVVocTF4ekNUWldac2hrVFFZSWs2aGkyeTU2d0lXWFptTDViZnlXTUxCRlVtT0ZWUHc2U1lMaVlPTVMzVGlkVlRTVFlJaVpSSVIwWkppRFFsbGoyRld3K09XVmJiM2syWktvM1VCYzFvRDF6MXlKbUVzM3ppREVXcEIxR0Q4a3VIbkN3R3o5cytUNHA2K2JQSnAwNFU2cUJzS2JFRVltaGhZdEczck1VdnlqWjRYWGtXa0ZHaHJHSXQzVUx2aUtXM2FKbGtpMkdQZnFnYWNyUFlFMGZqSEhuVEQrMFIzbkhmV202V1hSclBBNFkyTzF3V1FpSHV4VzVHZXNBTiszNkdVaFg2cUJWekRQM216R0Q5cTQ5KzdnNEhENWFvQTFrYjdlcU03RjNnMVlEZHdVRUI4WXJ0ZS8rdTVKZkhpaU5QS2dkWHJMRFVPZUJoRDR0MnVxdFY2N2RuaDlHV2l5MCtIejNTeGhtdGs0NlFqNWFUN0NwcU9SK1VRSm1wZFFiUDRWbmh1NEllcHAvTkJydHdyekNVYkFpckpLUzF2YWZUWmtqTDNPS21MendBZzNCOG9UWUxhRW5ZPQ=="\
#            ,'427潭子區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/da107de1ae0e05b83829785b652f53dc?q=VTJGc2RHVmtYMStMRmRIR2JhWWxibWkyWG03U0k0U2Z4VFlCanFCU091clRXQUJYSC9aTHlKTmxoNGUxYmd4dDRaNXhubS9kWnpkaXZITVJqYU1UTGpuTk5pbGd2aFA2ek90N2tsMVJzelJxdEswNDIwUCs2TVpJYUZpMDdudDRoTnljbUFMdVRFeGxvZnZveXZ0QzgycUFScEZYU1drTk9xaE9Xc2wwSzRXb1JJNDZCcmZFaWNiaDYzVStrb1psYTk3VExUeHhMUDRyYVY2K3MxQXQwNGM1SDUxZk1aU1dYL21pZG51UkJ3WjhrejczWm9PMGh6VEZ1ZlFUZURYVTd6NEd3WHg4c051cm5TNVVQeDR3QWFZSS9nYUNsaEJPZ0pLazA1S0J4R3hlSTlnUVZOT05lQmljSUpxVy8yTGJnanlRT1d6alBIQkx2V3d3MERib04xMS9WK3NqUWxTKzVnck9KSHR4b1pkajRqWDVBT2hBMFdZOTJmL3lCNUxBdWdiSlhLTDB1eUpNSDlxcDFhVUNTMXBmS0ZVMGFad1lEdEhBSk5aV2ZIVlcrM0RqektDZ0FjRkVQcm5MSDBoSnFmVkV6cmdBWURMdTl1NUhhWFMvaDBqWkdJVFlEWXBUdTNmOVNYc1l0RVVHV0xJejNnRHNnOFNENTI4RnlpdXNsOGcwLzlrVkdYaEJsbERJV3VzOTk5UHNSWENuZFJOYVUzd0l5NEtlZVJrPQ=="\
#            ,'434龍井區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/12a01481900570acc5f8fa16ece80ddf?q=VTJGc2RHVmtYMThwRGRieGpwYkk2UE5iK0phNVRPajU4ZUxHQy9SYytHbUtZWXk0SWNWWVdFb0xtVGwydVFkVjltSThLdTdzUlpxTlFuUzRHbXJLU2hGVjI4UmhRUXBNdXBFYlVYTWdGb3g0WmRjVlZrLzlXMlpEVGt5NzFTSGRSWTZNVGpGMEJ0b2JzMFVYZ3FkODArSDBwZWFwRmh6bzU0VzRjc0czY1NaV0Z3QlJZN1ZDTmJDeFlSRjZFdjJqdGRiMmNYYnZYMEs2T3RwZDdoZTg3SlVpMEU4Uy9HU2ZJS0tBZitUTHRWNWRvMFBiVE9mSC9aNkpBVTd4bjVqNmNVZTJVb0FtM0dKK3pFdG03clZDOFhqN2tHdGMzbS9kS2orRjM0RTVERU9SUVpkK3VUbkFQbTAvL3krOTZMelNQSW9GS0xlaWthbmhUWjBXQlVQaEhSaWRRY3hYVnF5bnoxYkFXbVk4aytrZ1VDV3JOK1BqZ3lhSXdydzFzUnM1UHdNcmxPQ0Vjb1BpTzVBS3ZWYVNoeFdkMFVwRy96TGlTbVEyQ2Y5emRad244VHA0V2ZzTGJVSXJacUxWYjZtNnFNbCtkN1owa3pRZ1hjZXUzOHNUWHZsdkFrcXg2dTdva3FjOFBOckZ0S0lZN3NPUDY2ODliRk92QU5OdGtjSFp0ODVZTXFrVHdQNW0vcjZEdHV0VEF5ZXpsUFdlMlRWN3FsZUpWQnFIalk0PQ=="\
#            ,'420豐原區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/e53a7294d45a9c25feab1d6b6b0afc28?q=VTJGc2RHVmtYMTlaWklmQmZTSjRjY3pJWDhrTFlja241cDVRN3ZOTjg2bUtvcHJJQytNK2Fya2hMY3NYZG1Oa0RHSFQ1Slh3QmpKZmhSNjl2TlhXZDlmRStvSTRxT2xjd0FSYkZVa1lydC9qMUtGUEVTU043aUFuV2g0dUd4TmRiTjloZmEvYS9nSEtFazJhT3FQaVg4bVJKY2k0M2JtT1RaeGxNejhCeDZubDZKZDJEck9mQnBJYlgxUXQwQ3pXZVJpREVxakcyUERDakVWbGsvZkIzSmpYdnhtSU1sSHd5UE42eHBvM1o3dUNQZnovMEw5Z0Q0aW9QNW01bnhQSzJIbVRSaGdxeGlMakR4aGxGQXlZQVhDaXFwT3hIY2xuekZMbFdOclNZZXc3a0F0MWRoVDhJLzhUVTJmNzNILzlmelJ0WnBHa3hIbElhVjN5K25DUnljTnJoZ2xqZ1NzMnU4eTRPaGFCeTJ0cEZKeWd1VDVsYWMxZnZrNGNjbUlud1V4V2p3OFV6RnY2R3lZRE43WkNjMENHWTMvTkMrWG84cStCQU40MmVTMUtyOFFTRHB1RUpLZHJKNVdCT0hiSzJZcVNwd0lxWkt6djFBVFRPQkRUQnU1eUdvU0tsZkdBRjRSQUVjWEtRd250WVpmblRxdXMwYXJOM0lDT1BzVTJqQVc2WHgwbWx6ZngxUFVQY1gxaTdXL25DdE96ejl0emhsWG52ZjdxU1ZrPQ=="\
#            ,'413霧峰區':"https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/855b9e512fecbeb83dd4279fbe01de65?q=VTJGc2RHVmtYMS9ycFhiWVRYRmZXRkpPUjYxWHNYc0F1c205Y2xhalB5cmk3Y2l0a3Yrdjh2UnQrUzlvaWJUc2VkNjlLK00wQnFnUUZSaFhUUmhYT2pGUDJxeGVmRnUydExHWGx5L28rU3BleDUzQy9PVUE3NVpyeTVPTFFjc2VSazBGaVh2MlNZZ3Mxd3NNT2t5cmlBcVlWeGJ4eHJiNHJmZEZ5MkdhdkJFOWpaSTVoSXBqV09QYms1d21BcGNXRDlHbEwxVWl4MEcxWUR6UkVsQXU3VzRudTNHNjRyc3Q3bWgzL2lWVWluTzR5WXZWd2ZBUUE0QmJ1aXl3aHhvUWpqUWJFZTB3ZWNrNFRycENJaDJPcXlLbThpbjlhQ3ZkaHNYdTIrbmgweGdLNXJIMkNUeTlvL2psdUkxeHgrS3VqcnZJWlVqQ3VLejhhTkEyTEs1d1QvRkxGMXNiSTdxOHowMTB5alFMZ2dSd0daYzZqT0xhK3E3NkhJMUJUU2QzZW5VSkEzcGUzbnUycTJBZVdPR05OMmtoWE54VmRrTXJhY2NqaXY0bENEZ2xMMml0TVVEUktBT3dibWM0K0txN3NvZGRXVC9Ld3Zyc3FiYU9JNTgySUltSXdOc1ZWeFhkengxaTliUGpQVk05ZFpjM2dxcGxlZ3pWNDBzVm0xSFpadHYwbHpFRENIdm0yYWp6bDUwc2E5LzFwYXA3b29Cd1EyR2dXRkZRcEI0PQ=="\
#         }
#     
# =============================================================================
