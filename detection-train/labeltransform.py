from tqdm import tqdm
from pathlib import Path
import cv2
loacalLabels = ["sly_bjbmyw","sly_dmyw","hxq_gjbs","hxq_gjtps","hxq_yfps","ywzt_yfyc","ywzt_yfzc",
            "bj_wkps","bj_bpps","bj_bpmh","bjdsyc_zz","bjzc","gcc_mh","gcc_ps","yw_nc","yw_gkxfw",
            "cysb_cyg","cysb_sgz","cysb_tg","cysb_lqq","cysb_qyb","qtjdq","ylsff","dl","pzq",
            "jyh","drq","ddjt","yx","jdyxx","jyz","ecjxh","hxq","SF6ylb","xldlb","ylb","ywb",
            "ywj","ws_ywyc","ws_ywzc","ws_ywwz","yljdq_flow","yljdq_stop","fzh_f","fhz_h","fhz_ztyc",
            "hxq_gjzc","pzqcd","jyhbx","drqgd","jyz_pl","yxdgsg","jdyxxsd","bmwh","bjdsyc_sx","xmbhyc",
            "xmbhzc","kgg_ybf","kgg_ybh","kk_f","kk_h","zsd_l","zsd_m","mbhp","jsxs_ddjt","jsxs_ddyx","jsxs_jdyxx","jsxs_ecjxh","cc"]



detect_dict = {
    "sly_bjbmyw": 0,"cysb_cyg":0,"cysb_sgz":0,"cysb_tg":0,"cysb_lqq":0,"cysb_qyb":0,"qtjdq":0,"ylsff":0,
    "sly_dmyw": 1,
    "jyz_pl": 2,"jyz":2,
    "jsxs_ddyx": 3,#金属锈蚀-导电接头
    "bmwh": 4,
    "bj_wkps": 5,
    "bjdsyc_sx": 6,
    "yw_nc": 7,
    "yw_gkxfw": 8,
    "mbhp": 9,
    "xy": 10,#吸烟
    "wcgz": 11,#未穿工装
    "wcaqm": 12,#未穿安全帽
    "pzq": 13, "pzqcd": 13,
    "jyh": 14, "jyhbx": 14,
    "drq": 15, "drqgd": 15,
    "yx": 16, "yxdgsg": 16,
    "jdyxx": 17, "jdyxxsd": 17, "jsxs_jdyxx": 17,#金属锈蚀-接地引下线
    "ddjt": 18, "jsxs_ddjt": 18,#金属锈蚀-导电接头
    "ecjxh": 19, "jsxs_ecjxh": 19,#金属锈蚀-二次接线盒
    "xmbhyc": 20, "xmbhzc": 20,
    "kgg_ybf": 21, "kgg_ybh": 21,
    "fzh_f": 22, "fhz_h": 22, "fhz_ztyc": 22,
    "hxq_gjbs": 23, "hxq_gjzc": 23, "hxq_gjtps": 23,"hxq":23,
    "ywzt_yfyc": 24, "ywzt_yfzc": 24, "hxq_yfps": 24,
    "bjzc": 25, "bj_bpps": 25, "bjdsyc_zz": 25, "bjdsyc_ywj": 25,#表计读数异常-油位计
    "bjdsyc_ywc": 25,#表计读数异常-油位窗
    "bj_bpmh": 25, "gcc_mh": 25,"gcc_ps": 25, "SF6ylb": 25,
    "xldlb": 25, "ylb": 25, "ywb": 25, "ywj": 25, "ywc": 25,#油位窗
    "ws_ywzc": 25, "ws_ywyc": 25,"ws_ywwz":25,"yljdq_flow": 25,
    "yljdq_stop": 25,
    "kk_f": 26, "kk_h": 26,
    "zsd_l": 27, "zsd_m": 27
}



def getPath(targetDir, globStr, targetDirList=None):
    if targetDirList is None:
        targetDirList = list()

    childDirList = list(targetDir.iterdir())
    for childDir in childDirList:
        if childDir.is_dir():
            targetDirList = getPath(childDir, globStr, targetDirList)

    targetList = list(targetDir.glob(globStr))

    if len(targetList) > 0:
        targetDirList = targetDirList+targetList
        return targetDirList
    else:
        return targetDirList

imgDirList = [
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v1_v2/labels"), #v1_v2
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v3/labels"), #7207
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v4/labels"), #v4 8427
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v5/labels"), #v5
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v6/labels"), #v6
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v7/labels"),
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v8/labels"),
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v9/labels"),
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v10/labels"),
    Path("/media/industai/DATA1/data/国网全国比赛数据/赛道一公司标注数据/gdwDatasets/v11/labels"),]
pathList = []
for idx,imgDir in enumerate(imgDirList):
    globStrList_pic = ['*.txt']
    for globStr in globStrList_pic:
        pathList = pathList + getPath(imgDir, globStr)

if __name__ == '__main__' :
    for txtPath in tqdm(pathList):
        txtParents = txtPath.parent.parent / "tc_txts"
        txtParents.mkdir(parents=True,exist_ok=True)
        txtName = txtPath.name
        newPath = txtParents / txtName
        ff = open(str(newPath),"w",encoding='utf-8')
        f = open(str(txtPath),encoding='utf-8')

        for line in f.readlines():
            strline = line.split(" ")
            if loacalLabels[int(int(strline[0]))] in detect_dict:
                newLabelNumber= detect_dict[loacalLabels[int(strline[0])]]
                strline[0] = str(newLabelNumber)
                newStrLine=" ".join(strline)
                ff.write(newStrLine)
        ff.close()

