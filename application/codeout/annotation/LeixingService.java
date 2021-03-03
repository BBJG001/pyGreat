package com.service;
     
import java.util.GregorianCalendar;

import com.dao.TLeixingDAO;
import com.dao.TShebeiDAO;

//类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始类开始
public class LeixingService {
	private TLeixingDAO TLeixingDAO;	// 行内注释
	private TShebeiDAO	TShebeiDAO;		/* 行内注释2 */
	/*
	多行
	测试
	*/
	public TLeixingDAO getTLeixingDAO() {
		// zheli 
		return TLeixingDAO;
	}
	/**
	*多行
	*测试
	*/	
	
	public void setTLeixingDAO(TLeixingDAO leixingDAO) {
		TLeixingDAO = leixingDAO;
	}
	
	public TShebeiDAO getTShebeiDAO() {
		return TShebeiDAO;
	}

	public void setTShebeiDAO(TShebeiDAO shebeiDAO) {
		TShebeiDAO = shebeiDAO;
	}
	
	//根据类型ID获取该设备编号
	public String getSbhbByLxid(String id){
		String result = "";
		try{
			String sql = "select qianzhui from TLeixing where id="+id;	//获取类型前辍
			Object obj = (Object)(TLeixingDAO.getHibernateTemplate().find(sql).get(0));
			
			sql = "select count(lxid) from TShebei where lxid = "+id;		//获取要添加的设备是该类型的第几个
			Object objnum = (Object)(TLeixingDAO.getHibernateTemplate().find(sql).get(0));
			int num = Integer.parseInt(objnum.toString());
			
			String bhNum = getBhNum(String.valueOf(++num));
			
			GregorianCalendar gc = new GregorianCalendar();
			
			result = obj.toString()+gc.get(GregorianCalendar.YEAR)+bhNum;
		}catch(Exception e){
			e.printStackTrace();
		}
		
		return result;
	}
	
	private String getBhNum(String num){
		String result = "";
		for(int i=0;i<(3-num.length());i++){
			result += "0";
		}
		result += num;
		return result;
	}
}
