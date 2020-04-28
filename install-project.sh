cd ~/data/Github/
sleep $(shuf -i 1-100 -n 1)
rm -rf shapeology_code
git clone -b kui_dev --single-branch https://github.com/yoavfreund/shapeology_code.git
source shapeology_code/configure.sh
# aws s3 cp --recursive $ROOT_DIR/CSHL_shift/MD594/ 's3://mousebrainatlas-data/CSHL_shift/MD594/'
# aws s3 cp --recursive $ROOT_DIR/CSHL_region_features/MD594/ 's3://mousebrainatlas-data/CSHL_region_features/MD594/'
# aws s3 cp $ROOT_DIR/CSHL_shift/MD594/ 's3://mousebrainatlas-data/CSHL_shift/MD594/'
# aws s3 cp $ROOT_DIR/CSHL_region_features/MD594/ 's3://mousebrainatlas-data/CSHL_region_features/MD594/'
#python -m ipykernel install --user --name shapeology --display-name "shapeology"
pip install awscli
pip install shapely
pip install mxnet
cd shapeology_code/scripts/Cell_datajoint/

#python HSV_datajoint_v2.py 'AWS' 'MD589'
python Cells_extract_datajoint.py 'AWS' 'DK39'
#python Patch_extractor_datajoint.py 'AWS' 'MD585'
# python Sample_features_datajoint.py 'AWS' 'MD585'
#python Thresholds_datajoint.py 'AWS' 'MD589'
#python Sqlite_datajoint.py 'AWS' 'MD589'
# python Scoremap_datajoint.py 'AWS' 'MD594'
# python Cell_mark_datajoint.py 'AWS' 'MD594'