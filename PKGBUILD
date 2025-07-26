pkgname=votes
pkgver=1.0.0
pkgrel=1
pkgdesc="A simple tool that tells you how many votes an AUR package has"
arch=('any')
url="https://github.com/eshnd/votes"
license=('MIT')
depends=('python')
source=("$pkgname-$pkgver.tar.gz")
md5sums=('SKIP') 

package() {
  cd "$srcdir/$pkgname-$pkgver"
  install -Dm755 my-python-app.py "$pkgdir/usr/bin/my-python-app"
}

