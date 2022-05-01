## Available Filters
vol10k_fltr = (df['Volume'] > 10000)
nooi_fltr = (df['OI'] <= 0)
oi2k_fltr = (df['OI'] < 2500)
cp_fltr = (df['Price'] < 15.00)
price_fltr = (df['Last'] < 2.5)
price_fltr2 = (df['Last'] < 5.00)
dte_fltr = (df['Days to Exp'] > 3.0) ## Filter by Days to Expiration
call_fltr_delta = (df['Delta'] < 0.40)
call_fltr_delta2 = (df['Delta'] > 0.15) ## Filter by Delta
put_fltr_delta = (df['Delta'] > -0.40)
put_fltr_delta2 = (df['Delta'] < -0.15)
call_fltr = (df['Price'] < df['Strike']) & (df['Type'] == 'Call') ## Filter for Calls
put_fltr = (df['Price'] > df['Strike']) & (df['Type'] == 'Put') ## Filter for Puts

## Largest Size
val_250k_fltr = (df['Cash Value'] > 250000)
val_500k_fltr = (df['Cash Value'] > 500000)
val_1m_fltr = (df['Cash Value'] > 1000000)
val_5m_fltr = (df['Cash Value'] > 5000000)
val_10m_fltr = (df['Cash Value'] > 10000000)
val_25m_fltr = (df['Cash Value'] > 25000000)

call_df = (df[val_1m_fltr & call_fltr & dte_fltr & price_fltr2])
put_df = (df[val_1m_fltr & put_fltr & dte_fltr & price_fltr2])
main_df = (df[val_1m_fltr & vol10k_fltr & oi2k_fltr & price_fltr2])
big_df = (df[val_500k_fltr & price_fltr2])
big_calls = (df[val_1m_fltr & call_fltr_delta & call_fltr_delta2])
big_puts = (df[val_1m_fltr & put_fltr_delta & put_fltr_delta2])
top_filt = (df[val_250k_fltr & price_fltr][call_fltr | put_fltr])

aapl = df[df['Symbol'] == 'AAPL']
tsla = df[df['Symbol'] == 'TSLA']
nvda = df[df['Symbol'] == 'NVDA']
amc = df[df['Symbol'] == 'AMC']
asan = df[df['Symbol'] == 'ASAN']
ddog = df[df['Symbol'] == 'DDOG']
abnb = df[df['Symbol'] == 'ABNB']
adbe = df[df['Symbol'] == 'ADBE']
amd = df[df['Symbol'] == 'AMD']
fb = df[df['Symbol'] == 'FB']
pton = df[df['Symbol'] == 'PTON']
aal = df[df['Symbol'] == 'AAL']
ual = df[df['Symbol'] == 'UAL']
bac = df[df['Symbol'] == 'BAC']
jpm = df[df['Symbol'] == 'JPM']
bidu = df[df['Symbol'] == 'BIDU']
googl = df[df['Symbol'] == 'GOOGL']
nflx = df[df['Symbol'] == 'NFLX']
dkng = df[df['Symbol'] == 'DKNG']
docu = df[df['Symbol'] == 'DOCU']
fubo = df[df['Symbol'] == 'FUBO']
hood = df[df['Symbol'] == 'HOOD']
ccl = df[df['Symbol'] == 'CCL']
pltr = df[df['Symbol'] == 'PLTR']
fsr = df[df['Symbol'] == 'FSR']
crm = df[df['Symbol'] == 'CRM']
msft = df[df['Symbol'] == 'MSFT']
amzn = df[df['Symbol'] == 'AMZN']
mara = df[df['Symbol'] == 'MARA']
pfe = df[df['Symbol'] == 'PFE']
mnra = df[df['Symbol'] == 'MNRA']
snap = df[df['Symbol'] == 'SNAP']
riot = df[df['Symbol'] == 'RIOT']
lcid = df[df['Symbol'] == 'LCID']

## ETF
spy = etf_df[etf_df['Symbol'] == 'SPY']
qqq = etf_df[etf_df['Symbol'] == 'QQQ']
iwm = etf_df[etf_df['Symbol'] == 'IWM']
dia = etf_df[etf_df['Symbol'] == 'DIA']
tlt = etf_df[etf_df['Symbol'] == 'TLT']
arkk = etf_df[etf_df['Symbol'] == 'ARKK']
arkg = etf_df[etf_df['Symbol'] == 'ARKG']
arkf = etf_df[etf_df['Symbol'] == 'ARKF']
eem = etf_df[etf_df['Symbol'] == 'EEM']
emb = etf_df[etf_df['Symbol'] == 'EMB']
iyr = etf_df[etf_df['Symbol'] == 'IYR']
kre = etf_df[etf_df['Symbol'] == 'KRE']
gld = etf_df[etf_df['Symbol'] == 'GLD']
slv = etf_df[etf_df['Symbol'] == 'SLV']
soxl = etf_df[etf_df['Symbol'] == 'SOXL']
spxu = etf_df[etf_df['Symbol'] == 'SPXU']
uvxy = etf_df[etf_df['Symbol'] == 'UVXY']
vxx = etf_df[etf_df['Symbol'] == 'VXX']
xbi = etf_df[etf_df['Symbol'] == 'XBI']
xlb = etf_df[etf_df['Symbol'] == 'XLB']
xlc = etf_df[etf_df['Symbol'] == 'XLC']
xle = etf_df[etf_df['Symbol'] == 'XLE']
xlf = etf_df[etf_df['Symbol'] == 'XLF']
xli = etf_df[etf_df['Symbol'] == 'XLI']
xlp = etf_df[etf_df['Symbol'] == 'XLP']
xlv = etf_df[etf_df['Symbol'] == 'XLV']
xop = etf_df[etf_df['Symbol'] == 'XOP']
yinn = etf_df[etf_df['Symbol'] == 'YINN']
big_3_etf = pd.concat([spy, qqq, iwm])
faang = pd.concat([fb, aapl, amzn, nflx, googl])
cheap_giants = pd.concat([aapl, nvda, fb, msft])
expensive_giants = pd.concat([tsla, amzn, googl])
