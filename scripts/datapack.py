from datapackage import Package

package = Package()
package.infer('archive/data_imp.csv')
package.infer('data/csv_wrang.csv')
package.commit()
package.save('datapackage.json')