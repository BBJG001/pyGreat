package com.service;
     
import java.util.GregorianCalendar;

import com.dao.TLeixingDAO;
import com.dao.TShebeiDAO;

//�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ�࿪ʼ
public class LeixingService {
	private TLeixingDAO TLeixingDAO;	// ����ע��
	private TShebeiDAO	TShebeiDAO;		/* ����ע��2 */
	/*
	����
	����
	*/
	public TLeixingDAO getTLeixingDAO() {
		// zheli 
		return TLeixingDAO;
	}
	/**
	*����
	*����
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
	
	//��������ID��ȡ���豸���
	public String getSbhbByLxid(String id){
		String result = "";
		try{
			String sql = "select qianzhui from TLeixing where id="+id;	//��ȡ����ǰ�
			Object obj = (Object)(TLeixingDAO.getHibernateTemplate().find(sql).get(0));
			
			sql = "select count(lxid) from TShebei where lxid = "+id;		//��ȡҪ��ӵ��豸�Ǹ����͵ĵڼ���
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
