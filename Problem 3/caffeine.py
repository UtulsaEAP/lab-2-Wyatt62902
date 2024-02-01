
def caffeine():
    caffeine_mg = float(input())
    half_life6 = float(caffeine_mg / 2)
    half_life12 = float(caffeine_mg / 4)
    half_life24 = float(caffeine_mg / 16)
    print('After 6 hours: 'f'{half_life6:.2f}'+' mg')
    print('After 12 hours: 'f'{half_life12:.2f}'+' mg')
    print('After 24 hours: 'f'{half_life24:.2f}'+' mg')
    
if __name__ == "__main__":
    caffeine()