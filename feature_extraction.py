#feature extraction tool
import tldextract

# Extract features that can be derived from a URL
def extract_features(url):
    ext = tldextract.extract(url)
    features = {}
    
    features['DomainLength'] = len(ext.domain)
    features['TLDLength'] = len(ext.suffix)
    features['NoOfSubDomain'] = len(ext.subdomain.split('.')) if ext.subdomain else 0
    features['NoOfLettersInURL'] = sum(c.isalpha() for c in url)
    features['LetterRatioInURL'] = features['NoOfLettersInURL'] / len(url)
    features['NoOfEqualsInURL'] = url.count('=')
    features['NoOfQMarkInURL'] = url.count('?')
    
    return features
